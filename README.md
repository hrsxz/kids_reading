# kids_reading

An app that allows kids to scan the book's and read the book.

## Getting Started

### Prerequisites

#### Install FFmpeg for Eleven Labs' Play Audio Function

```python
from elevenlabs import generate, play

audio = generate(text, voice="DPsqCHWEBVTyO9962K8u")
play(audio)
```

#### Download ffmpeg (Window version)

  1. Download the appropriate version for Windows ([Go to the FFmpeg Download Page](https://github.com/BtbN/FFmpeg-Builds/releases)).

  2. Extract the files to a directory (e.g., C:\ffmpeg). And add ffmpeg to the System Path.
![alt text](miscellaneous/images//image.png)
  3. Verify Installation:

      ```powershell
      ffmpeg --version
      ```

#### Add key in environment variables

![alt text](miscellaneous/images//image-1.png)

#### Bugfix for pydub
  
  1. Open the file `pydub\utils.py` in the pydub package directory.
  ![alt text](miscellaneous/images/playback_bug.png)
  2. Add line *" f.close()*  # close the file stream" in the _play_with_ffplay function.

      ```python
      def _play_with_ffplay(seg):
        PLAYER = get_player_name()
        with NamedTemporaryFile("w+b", suffix=".wav") as f:
            f.close()  # close the file stream
            seg.export(f.name, "wav")
            subprocess.call([PLAYER, "-nodisp", "-autoexit", "-hide_banner", f.name])
      ```

### 发布Toga应用到iOS App Store

## 开发阶段

### 1. 安装必要工具

- 确保安装了Python（版本3.5及以上）。
- 安装Briefcase和Toga：

```bash
pip install briefcase toga
```

### 2.  创建应用

使用Briefcase创建Toga应用：

```bash
briefcase new
```

### 3.  开发应用

编辑src/<app_name>/app.py，开发应用逻辑和UI。示例代码：
```python
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER

def on_button_press(widget):
    print("Hello world!")

def build(app):
    button = toga.Button(
        'Press me!',
        on_press=on_button_press,
        style=Pack(padding=20)
    )
    return toga.Box(
        children=[button],
        style=Pack(direction=COLUMN, alignment=CENTER, flex=1)
    )

def main():
    return toga.App(
        'First Toga App',
        'org.beeware.helloworld',
        startup=build
    )

if __name__ == '__main__':
    main().main_loop()
```

### 4.  本地测试

在应用目录下运行应用进行测试：
  
  ```bash
  briefcase dev
  ```
