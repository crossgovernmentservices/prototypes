#!/usr/bin/env bash
# Gets govuk_elements
# Prepares it to be used with the app

set -ex

TMP=$(mktemp -d -t xgs_govuk_elements.XXXXXX)
DEST_ZIP=${TMP}/govuk_elements.zip
DEST=application/static/govuk_elements

# Get
curl -L https://github.com/alphagov/govuk_elements/archive/master.zip -o $DEST_ZIP
unzip $DEST_ZIP -d $DEST

# Prepare
for sassfile in $(find $DEST -name '*.scss'); do
  sed -i '/^@import .*/d' $sassfile
done

# find application/static/govuk_elements -type f -exec md5sum {} \; | md5sum

rm -rf $TMP
