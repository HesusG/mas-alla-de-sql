#!/bin/bash
# Bootstrap a new Slidev workshop with neobrutalist design system
# Usage: ./init.sh "Workshop Name" repo-name

set -e

WORKSHOP_NAME="${1:?Usage: ./init.sh \"Workshop Name\" repo-name}"
REPO_NAME="${2:?Usage: ./init.sh \"Workshop Name\" repo-name}"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PARENT_DIR="$(dirname "$SCRIPT_DIR")"

echo "Creating workshop: $WORKSHOP_NAME in $REPO_NAME/"

mkdir -p "$REPO_NAME"
cd "$REPO_NAME"
git init

# Copy structure
mkdir -p styles components layouts public/images snippets

# Copy design system files
cp "$PARENT_DIR/uno.config.ts" .
cp "$PARENT_DIR/styles/index.css" styles/
cp "$PARENT_DIR/components/"*.vue components/
cp "$PARENT_DIR/layouts/"*.vue layouts/
cp "$PARENT_DIR/package.json" .

# Generate slides from template
sed "s/{{WORKSHOP_NAME}}/$WORKSHOP_NAME/g" "$SCRIPT_DIR/slides.md.template" > slides.md

# Generate CLAUDE.md from template
sed -e "s/{{WORKSHOP_NAME}}/$WORKSHOP_NAME/g" \
    -e "s/{{WORKSHOP_DESCRIPTION}}/Workshop presentation/g" \
    -e "s/{{CONTENT_LANGUAGE}}/Spanish/g" \
    "$SCRIPT_DIR/CLAUDE.md.template" > CLAUDE.md

# Copy gitignore
cp "$PARENT_DIR/.gitignore" .

echo ""
echo "Done! Next steps:"
echo "  cd $REPO_NAME"
echo "  npm install"
echo "  npm run dev"
