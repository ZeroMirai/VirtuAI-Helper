## Use this code with obs and Vtuber studio

You can use this code with OBS to show the subtitle and use Vtuber studio to show Live2D by following this guide.

![example2_image](guide/example_2.gif)

1. Download [OBS](https://obsproject.com/), [Vtuber studio](https://denchisoft.com/), [EarTrumpet](https://eartrumpet.app/), [VoiceMeeter banana](https://vb-audio.com/Voicemeeter/banana.htm)(after you install VoiceMeeter banana you'll also need to restart your PC) and open VoiceVox.
2. For VoiceMeeter banana, we need to change voice output and voice input first.
   1. Open the Control Panel by pressing the `Windows key` and typing `Control Panel`. In the upper right corner, click on `View by` and select `Large icon`.
      
      ![guide_1](guide/1.png)
      ![guide_2](guide/2.png)
      
   2. Click on `Sound`, scroll down until you see `VoiceMeeter Input`, and then click on it. Finally, click `Set Default`.
      
      ![guide_3](guide/3.png)
      ![guide_4](guide/4.png)
      
   3. Click on `Recording` at the top, scroll down until you see `VoiceMeeter Aux Output`, click on it, and then click `Set Default`.
      
      ![guide_5](guide/5.png)
      ![guide_6](guide/6.png)
      
   4. The first time the program is opened, it would look like this.
      
      ![guide_7](guide/7.png)
      
   5. Click on each `A1` to deselect them on all five panels. Similarly, do the same with `B1`. It should now look like this.

      ![guide_8](guide/8.png)
      ![guide_9](guide/9.png)
      
   6. On the upper right corner, click on `A1` and select your speaker output (WDM is recommended).
       
      ![guide_10](guide/10.png)
      ![guide_11](guide/11.png)

   7. Now, click on `A1` for all VIRTUAL INPUTS. However, for VOICEMEETER AUX, you'll also need to click on `B1`.
       
      ![guide_12](guide/12.png)

3. For Vtuber Studio.
   1. Open the settings by double-clicking on the screen and then click on the gear icon located on the left side.
      
      ![guide_13](guide/13.png)
      
   3. Scrolldown until you see `Microphone Setting` check `Use microphone` and select `VoiceMeeter Output (VB-Audio VoiceMeeter VAIO)` by clicking on the `Microphone`.
      
      ![guide_14](guide/14.png)
      ![guide_15](guide/15.png)
      
   3. Go to Model setting at the top left corner(a people icon with a gear). Scroll down until you see `Mouth Open`. Click on `input` and select or type `VoiceVolumePlusMouthOpen`.
      
      ![guide_16](guide/16.png)
      ![guide_17](guide/17.png)
      ![guide_18](guide/18.png)
      
   4. **Optional**: In `Microphone Setting`, I recommend setting `Volume gain` to 20 and everything else is set to 0.
4. For OBS, we'll add subtitles to display the text, and for Vtuber studio, we'll use it to show Live2D.
   1. To add a subtitle, press `+` in the source, select `Text(GDI+)`, and name it as `Subtitle`.
      
      ![guide_19](guide/19.png)
      ![guide_20](guide/20.png)
      
   2. After adding the text source, a window will appear like this. You'll need to check `Read from file` and then click `Browse`.
      
      ![guide_21](guide/21.png)
      ![guide_22](guide/22.png)
      
   3. Navigate to `subtitle.txt`, which is located inside the `text_log` folder, and select it.
      
      ![guide_23](guide/23.png)
      
   4. Customize and configure the subtitle file according to your preferences, (For my recommendation, I suggest reducing the size of the text, setting `Alignment` to center and `Verticle alignment` to center, right-clicking on the text, navigating to `Tranform` and selecting `Center Horizontally`. Also, check `Outline`, set the outline size to 10-14, and change the outline color to black by clicking on `Select color`).
      
      ![guide_24](guide/24.png)
      ![guide_25](guide/25.png)
      ![guide_26](guide/26.png)

   5. To add Vtuber Studio, press `+` in the source, select `Window Capture` and name it as `Live2D`
       
      ![guide_27](guide/27.png)
      ![guide_28](guide/28.png)
      
   6. After adding the video source, a window will appear like this. Click on `Window`, select `[VTube Studio.exe]: VTube Studio`, on `Capture Method` choose `Windows 10 (1903 and up)`, and then click `OK`.
       
       ![guide_29](guide/29.png)
       ![guide_30](guide/30.png)
       
   7. Right-click on the preview screen, choose `Windowed Projector (Preview)`, and resize it as your desire.
       
       ![guide_31](guide/31.png)
5. Running the code, open EarTrumpet and scroll down to the bottom you'll see `VoiceMeeter Input (VB-Audio VoiceMeeter VAIO)`, right click on `Python 3.11.xx` and click on `change` icon, select `VoiceMeeter Aux Input (VB-Audio VoiceMeeter AUX VAIO)`.
   
   ![guide_33](guide/33.png)
   ![guide_34](guide/34.png)
   ![guide_35](guide/35.png)
   
6. Change your `playback/output device` by clicking on the speaker icon on the taskbar (or go to `window setting` -> `System` -> `Sound` -> `Choose your output device`). Select `VoiceMeeter Aux Input (VB-Audio VoiceMeeter AUX VAIO)` first and then selcet `VoiceMeeter Input (VB-Audio VoiceMeeter VAIO)` (we need to do this process to let Python recognize these playback devices).
   
   ![guide_36](guide/36.png)
   ![guide_37](guide/37.png)
   
7. In Vtuber Studio, open the settings, navigate to `Microphone Setting` and click on `Reload`.
8. Enjoy! your AI assistant!
