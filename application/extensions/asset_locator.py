class AssetLocator(object):

    def init_app(self, app):
        app.template_context_processors[None].append(self.locate)

    def locate(self):
        # /static/govuk_toolkit/ contains the SASS files
        # (more specifically: variables) to re-use within our own SASS
        #return {'asset_path': '/static/govuk_toolkit/'}

        # /templates/govuk_template/ contains the template we want to extend,
        # but also some pre-compiled CSS and JS.
        #return {'asset_path': '/templates/govuk_template/assets/'}

        # Hence, we just copy the pre-compiled assets from 'template'
        # to 'static', and use those.
        return {'asset_path': '/static/govuk_template/assets/'}
