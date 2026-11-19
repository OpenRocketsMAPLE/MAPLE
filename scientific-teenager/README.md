# The Scientific Teenager Discord app

This directory is the canonical GitHub deployment source for The Scientific Teenager Discord relay.

`source.tar.gz.b64` is the complete patched application source snapshot. The Dockerfile decodes and builds it reproducibly.

Current intended behavior:
- `/science` configures the public channel where the command is run.
- The install URL requests Discord's **Mention Everyone** permission.
- One YES vote approves a proposal; NO votes do not block approval.
- Approved partner posts are ordinary Discord messages.
- The first message uses a real `@everyone` mention.
- Original URLs are sent directly and visibly; Railway tracking URLs are not used for partner delivery.
- OpenRockets HQ proposal/review controls remain separate from partner setup.

Railway deploys from this GitHub directory. Runtime code is not reconstructed from environment-variable source bundles or startup patch scripts.
