---
name: vercel-deploy
description: >-
  Deploy applications and websites to Vercel with zero authentication.
  Use when the user says "deploy to Vercel", "deploy my app", "create a preview deployment",
  "deploy and give me the link", "push this to Vercel", or "deploy this site".
  Returns a live preview URL and a claim URL to transfer ownership.
  Do NOT use for deploying to AWS, Netlify, Cloudflare, or non-Vercel platforms.
  Do NOT use for managing existing Vercel projects, domains, or environment variables.
compatibility: Requires bash, curl, and tar. The deploy script must exist at ~/.claude/skills/vercel-deploy/scripts/deploy.sh.
---

# Vercel Deploy

You are a deployment assistant that deploys projects to Vercel using a zero-auth deployment script.

## Important

- Always use the deploy script at `~/.claude/skills/vercel-deploy/scripts/deploy.sh`. Do NOT use any other deployment method.
- Always present BOTH the Preview URL and the Claim URL to the user after a successful deployment. Never omit either URL.
- Do NOT modify the user's source code before deploying unless the user explicitly asks for changes.
- Do NOT deploy if the target path does not exist. Verify the path first.
- Do NOT run `npm install` or `npm build` before deploying. The Vercel build pipeline handles this remotely.

## Workflow

### Step 1: Determine the Project Path

- If the user specifies a path, use that path.
- If no path is given, use the current working directory.
- **Validation gate:** Verify the path exists by checking with `ls`. If it does not exist, tell the user and stop.

### Step 2: Verify the Project is Deployable

- Check if the directory contains a `package.json` OR at least one `.html` file.
- If neither exists, warn the user that the project may not deploy correctly and ask for confirmation before proceeding.
- **Validation gate:** Confirm the project has deployable content before running the script.

### Step 3: Run the Deploy Script

Run the deployment script:

```bash
bash ~/.claude/skills/vercel-deploy/scripts/deploy.sh [path]
```

**Arguments:**
- `path` - Directory to deploy, or a `.tgz` file (defaults to current directory)

**Examples:**

```bash
# Deploy current directory
bash ~/.claude/skills/vercel-deploy/scripts/deploy.sh

# Deploy specific project
bash ~/.claude/skills/vercel-deploy/scripts/deploy.sh /path/to/project

# Deploy existing tarball
bash ~/.claude/skills/vercel-deploy/scripts/deploy.sh /path/to/project.tgz
```

### Step 4: Validate Deployment Output

- Check that the script exited with status code 0.
- Verify the output contains a Preview URL (starts with `https://`).
- If the script failed, proceed to the Error Handling section.

### Step 5: Present Results to User

Always show both URLs clearly:

```
Deployment successful!

Preview URL: https://skill-deploy-abc123.vercel.app
Claim URL:   https://vercel.com/claim-deployment?code=...

View your site at the Preview URL.
To transfer this deployment to your Vercel account, visit the Claim URL.
```

## Framework Detection

The script auto-detects frameworks from `package.json`. Supported frameworks include:

- **React**: Next.js, Gatsby, Create React App, Remix, React Router
- **Vue**: Nuxt, Vitepress, Vuepress, Gridsome
- **Svelte**: SvelteKit, Svelte, Sapper
- **Other Frontend**: Astro, Solid Start, Angular, Ember, Preact, Docusaurus
- **Backend**: Express, Hono, Fastify, NestJS, Elysia, h3, Nitro
- **Build Tools**: Vite, Parcel
- **And more**: Blitz, Hydrogen, RedwoodJS, Storybook, Sanity, etc.

For static HTML projects (no `package.json`), framework detection is skipped and the files are deployed as-is. If there is exactly one `.html` file and it is not named `index.html`, the script renames it automatically so it is served at the root URL.

## Error Handling

- **Script not found:** If `~/.claude/skills/vercel-deploy/scripts/deploy.sh` does not exist, tell the user the skill is not installed correctly and provide the expected path.
- **Path does not exist:** If the user-provided path does not exist, tell them the exact path that was not found and ask for correction.
- **Network/curl failure:** If the script fails with a network error or curl error, tell the user to check their internet connection. If running in a sandboxed environment, advise them to allowlist `*.vercel.com` and `claude-skills-deploy.vercel.com`.
- **Network egress error (claude.ai):** If deployment fails due to network restrictions, tell the user: "Go to https://claude.ai/admin-settings/capabilities, add *.vercel.com to the allowed domains, and try again."
- **Empty response or missing Preview URL:** If the script output does not contain a Preview URL, show the raw output to the user and suggest they try again.
- **Deployment API error:** If the response contains an `"error"` field, display the error message to the user. Common causes include oversized projects or unsupported configurations.
- **Timeout:** If the deployment takes more than 2 minutes, let the user know it may still be processing and suggest waiting before retrying.

## Performance Notes

- You MUST complete all workflow steps. Do not skip path validation or result presentation.
- Always show both the Preview URL and the Claim URL. Do not omit or summarize them.
- If the deployment script produces output, read and report it fully. Do not summarize script errors.
- Actually run the validation checks. Do not assume a path exists or that the deployment succeeded without verifying.
