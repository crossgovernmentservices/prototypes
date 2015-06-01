;(function ( $, window, document, undefined ) {

  // Create the defaults once
  var pluginName = 'ical',
      defaults = {
        parent_selector: "[itemscope]",
        separator: " "
      };

  var content = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:HTML"
      ],
      content_end = [
        "END:VCALENDAR"
      ];
    

  function Plugin( element, options ) {
    this.element = element;

    this.options = $.extend( {}, defaults, options) ;

    this._defaults = defaults;
    this._name = pluginName;
    this.eventnodes = [];

    this.init();
  }

  Plugin.prototype.init = function () {
    var plugin = this;
    var $link = $(plugin.element);

    // determine if link is child of vevent node or refers
    // to another node and/or multiple nodes
    if(plugin.element.hasAttribute("data-ical-nodes")) {
      var eventnodes = $link.data("ical-nodes").split( plugin.options.separator );
      $.each(eventnodes, function(ind, item) {
        plugin.eventnodes.push( $("[data-ical-event=" + item + "]") );
      });
    } else {
      plugin.eventnodes.push( $link.parents( plugin.options.parent_selector ) );
    }

    $.each(plugin.eventnodes, function(ind, $vevent) {
      if ( $vevent.attr("itemtype") === "http://microformats.org/profile/hcalendar#vevent"  ) {
        plugin.fetchVEventProperties( $vevent );
      }
    });

    var full_content = content.concat(content_end);
    $link.attr("href", 'data:text/calendar;component=vevent,' + encodeURI(full_content.join("\r\n")))
  };

  Plugin.prototype.fetchVEventProperties = function ($vevent) {
    var plugin = this;

    content.push("BEGIN:VEVENT");
    content.push( plugin.creationDate() );

    $vevent.find("[itemprop]").each(function(ind, el) {
      content.push( plugin.addItemProp($(el)) );
    });

    content.push("END:VEVENT");
  };

  Plugin.prototype.addItemProp = function ($el) {
    var prop = $el.attr("itemprop").toUpperCase(),
        value = "";

    if( prop === "DTSTART" || prop === "DTEND" ) {
      value = $el.attr("title");
      prop = prop + ';TZID="Europe/London"';
    } else {
      value = $el.text();
    }
    return prop + ":" + value;
  };

  // create timestamp of file creation
  Plugin.prototype.creationDate = function () {
    var stamp = new Date();
    var stampString = '' + stamp.getUTCFullYear()
                        + ("0" + (stamp.getUTCMonth() + 1)).slice(-2)
                        + ("0" + stamp.getUTCDate()).slice(-2)
                        + 'T'
                        + stamp.getUTCHours()
                        + stamp.getUTCMinutes()
                        + stamp.getUTCSeconds()
                        + 'Z';
    return "dtstamp".toUpperCase() + ":" + stampString;
  };

  // plugin wrapper
  // prevents mulitple instantiations
  $.fn[pluginName] = function ( options ) {
    return this.each(function () {
      if (!$.data(this, 'plugin_' + pluginName)) {
        $.data(this, 'plugin_' + pluginName, 
        new Plugin( this, options ));
      }
    });
  }

})( jQuery, window, document );
