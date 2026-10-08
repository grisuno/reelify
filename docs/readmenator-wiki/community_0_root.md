# root

*Community 0 | 2 files | cohesion 1.00*

## Definition

This community groups 2 file(s) rooted at `root` with dominant language py (cohesion 1.00). Central symbols: `create_short_videos`, `crop_and_resize_clip`, `list_and_select_video`, `main`. Core file: `app.py` (4 symbols). Documented purpose: Autor: Gris Iscomeback Correo electrónico: grisiscomeback[at]gmail[dot]com Fecha de creación: xx/xx/xxxx Licencia: GPL v3  Descripción:.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `app.py` | py | utility | 4 | yes |
| `install.sh` | sh | utility | 0 | no |

## Key Symbols

- `crop_and_resize_clip` (function, `app.py:18`) `def crop_and_resize_clip(clip, left_half)`
- `create_short_videos` (function, `app.py:39`) `def create_short_videos(input_path, output_prefix, durations)`
- `list_and_select_video` (function, `app.py:69`) `def list_and_select_video()`
- `main` (function, `app.py:89`) `def main()`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 0
- Cross-boundary resolved imports (EXTRACTED): 0

## Connections

- No cross-community bridges recorded. This community is self-contained.

## Risks

- No scoped security, taint, cycle, or layer risks.

## Open Questions

- Why do 1 file(s) lack file-level docs (e.g. `install.sh`)? What purpose do they serve?
- What would break if the most connected file in root changed?
- Should root be split, given cohesion 1.00?

## Sources

- `app.py`
- `install.sh`
