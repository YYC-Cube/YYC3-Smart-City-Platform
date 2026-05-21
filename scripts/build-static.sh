#!/bin/bash
set -e

PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
API_DIR="$PROJECT_DIR/app/api"
API_BACKUP="$PROJECT_DIR/.api-backup"

echo "🔧 YYC³ Smart City - Static Export Build"
echo "========================================="

cleanup() {
  if [ -d "$API_BACKUP" ]; then
    echo "📦 Restoring API routes..."
    mv "$API_BACKUP" "$API_DIR"
  fi
}

trap cleanup EXIT

if [ -d "$API_DIR" ]; then
  echo "📦 Temporarily moving API routes (incompatible with static export)..."
  mv "$API_DIR" "$API_BACKUP"
fi

echo "🏗️  Building static export..."
NEXT_STATIC_EXPORT=true pnpm run build

echo "✅ Static export build complete! Output: ./out/"
