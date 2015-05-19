#!/usr/bin/env bash
echo "Running Heroku-specific commands..."
rm -rf /app/.bundle
make govuk_assets_all
