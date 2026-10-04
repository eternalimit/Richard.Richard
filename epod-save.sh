#!/bin/bash
echo "Synchronizing ledger and repository..."
git add .
git commit -m "Automated synchronization via epod-save.sh"
git push origin main
echo "Synchronization complete."
