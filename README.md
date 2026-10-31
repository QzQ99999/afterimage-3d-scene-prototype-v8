# Afterimage 3D scene prototype V8 — frozen release

User-approved snapshot preserved on 2026-11-01. Changes, rebuilding, replacement or redeployment require the owner's new explicit confirmation.

- [Play the frozen V8](https://qzq99999.github.io/afterimage-3d-scene-prototype-v8/)
- Original HTML size: 165,512,121 bytes.
- SHA-256: `8294e7e9d86bd670ec3382fb75f06091608bccfd4a0c60ade7a62ec2fe6a1fcb`

The HTML exceeds GitHub's normal individual Git-file limit. `snapshot/` stores a losslessly compressed, checksummed copy in small parts. `python restore_snapshot.py` restores `site/index.html` byte for byte; it does not compile or modify the scene. GitHub Pages serves that exact restored HTML.

Use a WebGPU-capable desktop browser. This snapshot retains the current visuals, combat, debris, and known performance limitations; the upper-right enemy status display is removed. Stable100FPS during all heavy-debris interactions is not guaranteed.

The initial Pages publication is explicitly authorized. The publication workflow has manual dispatch only; it must be disabled, along with repository Actions, after verified publication. No push-triggered or scheduled deployment is permitted. The game sources and full local frozen backup remain preserved locally.

Third-party assets retain their original ownership. The included Three.js license applies to Three.js; this repository does not grant new rights to supplied character, weapon, texture or VFX assets.
