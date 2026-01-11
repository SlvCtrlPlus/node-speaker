# Publishing Guide

This guide explains how to publish a new version of `node-speaker` with prebuilt binaries using GitHub Releases.

## Prerequisites

1. **GitHub Access**: You must have push access to the repository and permissions to create releases
2. **GitHub Token**: The default `GITHUB_TOKEN` is automatically provided by GitHub Actions

## Publishing Process

### 1. Prepare the Release

1. Update the version in `package.json`:
   ```bash
   npm version patch  # or minor, or major
   ```

2. Update `History.md` with the changes in this release

3. Commit the changes:
   ```bash
   git add package.json package-lock.json History.md
   git commit -m "Prepare for vX.Y.Z release"
   ```

### 2. Create and Push Tag

The prebuild workflow is triggered when you push a tag starting with `v`:

```bash
git tag v0.5.6  # Use your actual version number
git push origin master
git push origin v0.5.6
```

### 3. Monitor GitHub Actions

1. Go to the [Actions tab](https://github.com/SlvCtrlPlus/node-speaker/actions) on GitHub
2. Wait for the "Prebuild" workflow to complete
3. The workflow will:
   - Build N-API binaries for all supported platforms (6 builds total)
   - Each binary works across all Node.js 18+ versions thanks to N-API
   - Upload the binaries as artifacts
   - Create a GitHub Release with:
     - Complete package tarball with all prebuilds
     - Individual `.node` binaries for each platform
     - Auto-generated release notes

### 4. Verify Publication

1. Check that the release was created:
   - Go to [Releases](https://github.com/SlvCtrlPlus/node-speaker/releases)
   - Verify the new version is listed
   - Check that all prebuilt binaries are attached

2. Test installation from GitHub:
   ```bash
   # Install from GitHub release
   npm install https://github.com/SlvCtrlPlus/node-speaker/releases/download/v0.5.6/speaker-v0.5.6.tgz
   
   # Or install from git tag
   npm install github:SlvCtrlPlus/node-speaker#v0.5.6
   ```

## Manual Prebuild (Testing)

To test the prebuild process locally before publishing:

### Single Platform

Build for your current platform:

```bash
npm run prebuild
```

This creates binaries in the `prebuilds/` directory.

### All Platforms (Cross-compilation)

Build for all platforms using Docker:

```bash
npm run prebuild-all
```

Note: This requires Docker and can take significant time.

### Test Local Prebuild

After creating local prebuilds, test that they install correctly:

```bash
# In another directory
npm install /path/to/node-speaker
```

The installation should use the prebuilt binary instead of compiling.

## Troubleshooting

### Build Failures

If the GitHub Actions build fails:

1. Check the build logs in the Actions tab
2. Common issues:
   - Missing dependencies on specific platforms
   - Node version compatibility
   - Architecture-specific compilation issues

### GitHub Release Failures

If creating the GitHub Release fails:

1. Verify repository has "Read and write permissions" for workflows:
   - Go to Settings → Actions → General → Workflow permissions
   - Select "Read and write permissions"
2. Check that the tag was pushed correctly
3. Ensure no release already exists for that tag

### Prebuilds Not Found During Installation

If users report compilation from source when prebuilds should exist:

1. Verify prebuilds exist in the GitHub Release assets
2. Check that the platform/Node version is supported
3. Ensure users are installing from the release tarball, not directly from git
4. For git installations, prebuilds must be committed or users need to build from source

## Security

- The `GITHUB_TOKEN` is automatically provided by GitHub Actions
- No manual token configuration needed for GitHub Releases
- Limit repository write access to trusted maintainers
- Review workflow permissions regularly

## Optional: Publishing to npm

If you later decide to also publish to npm, you can:

1. Add `NPM_TOKEN` to GitHub Actions secrets
2. Uncomment the npm publish step in `.github/workflows/prebuild.yml`
3. Follow the standard npm publishing process

## Support

For issues with the publishing process:

1. Check existing GitHub Issues
2. Review the [RELEASE-CHECKLIST.md](RELEASE-CHECKLIST.md)
3. Contact the package maintainers

