# Polyglot Codebase Knowledge Graph

> Generated offline by **readmenator**. Supports C, C++, Python, Go, Rust, JS/TS, Java, C#, Shell, PHP, Dart, GDScript, Nim, ASM.
> No LLMs. No tokens. Pure static analysis.

**Total Files Parsed:** 2 | **Total Symbols Extracted:** 4 | **Total Imports:** 4

## Structural Knowledge Map
```mermaid
graph TD
    classDef mod fill:#1e1e1e,stroke:#ff6666,stroke-width:2px,color:#fff;
    classDef cls fill:#2d2d2d,stroke:#4ec9b0,stroke-width:2px,color:#fff;
    classDef fn fill:#333,stroke:#dcdcaa,stroke-width:1px,color:#dcdcaa;
    classDef ext fill:#111,stroke:#666,stroke-dasharray: 5 5,color:#aaa;
    app_py["app.py (py)"]
    class app_py mod;
    app_py_crop_and_resize_clip["crop_and_resize_clip"]
    class app_py_crop_and_resize_clip fn;
    app_py --> app_py_crop_and_resize_clip
    app_py_create_short_videos["create_short_videos"]
    class app_py_create_short_videos fn;
    app_py --> app_py_create_short_videos
    app_py_list_and_select_video["list_and_select_video"]
    class app_py_list_and_select_video fn;
    app_py --> app_py_list_and_select_video
    app_py_main["main"]
    class app_py_main fn;
    app_py --> app_py_main
    install_sh["install.sh (sh)"]
    class install_sh mod;
    ext_cv2["cv2"]
    class ext_cv2 ext;
    app_py -.->|imports| ext_cv2
    ext_numpy["numpy"]
    class ext_numpy ext;
    app_py -.->|imports| ext_numpy
    ext_moviepy_editor["moviepy.editor"]
    class ext_moviepy_editor ext;
    app_py -.->|imports| ext_moviepy_editor
    ext_os["os"]
    class ext_os ext;
    app_py -.->|imports| ext_os
```

---

## Architecture Reference

### PY (1 files)

#### `app.py`
**Path:** `app.py`

**Functions:**
- `crop_and_resize_clip` (line 18)
- `create_short_videos` (line 39)
- `list_and_select_video` (line 69)
- `main` (line 89)

### SH (1 files)

#### `install.sh`
**Path:** `install.sh`

*No symbols extracted*
