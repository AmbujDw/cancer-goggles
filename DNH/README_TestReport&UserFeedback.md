Test Report & User Feedback
 
 
I updated the local repository on Raspberry Pi on June 29th, 2022, and the test report and user feedback are based on the updated repository.

I tested the tested following things,
•	Navigation in the GUI 
•	Options selection in GUI
•	GUI options, Exposure, Disparity
•	GUI options Opacity, Register
•	View Settings Lase Watts
•	Thresholding for Segmentation
•	Changing Resolution
•	Position change

The current operation and testing are being done with a three click computer mouse and keyboard, in the future it will be replaced by a pedal or similar device which would be more surgeon friendly in the operating room.
The application is currently only running when one CSI and one USB camera are connected. 
The left and right click mentioned in this report refer to the computer mouse left and right click because currently we use a computer mouse on the application.

The operator can select a GUI option by right clicking on it. But when the operator left clicks on the GUI option and then left clicks outside the GUI features then also the GUI option is selected.
When the operator middle clicks after selecting an option using right click, it highlights other options one by one on every click, in the sub-parts of GUI, but this is not uniform, it only happens sometimes.

If we want to change the resolution, then we must update the vertical and horizontal pixel values in the AppOptions.json file.

There is a built-in feature that after we update anything in the AppOptions.json then we can press home button when we are in the HMDOpView application, to apply the changes, but this feature is not working. Currently, we must restart the application to apply the changes. 
We have the option to change samples being examined, from sample 1 to sample 2 to sample 3. To change from one sample to another, there must not be any other GUI feature selected. We should be on the home screen without anything selected, then by pressing the middle click we enter the feature to select the sample and by pressing left or right click we can change the sample number, then by pressing the middle click again we can enter that sample number.

Even though we can change sample numbers, we cannot currently maintain separate options applied to different sample numbers. The features applied to the original sample number carries on to the next changed sample. The sample number GUI is created but it should also be correctly applied to the GUI and software so that we can remove this error.

Left clicking on a GUI option and then left clicking outside the GUI features, on the black screen also selects that option.

Right clicking on outside the GUI features let us move to a different option in the GUI without being selected but since there is no option of selecting that new highlighted option without the right click so this feature is not of much use. This feature is useful if the operator wants to see the other GUI options available without disturbing the current applied settings.

We can turn on or off the threshold applied for segmentation for either of the camera. Currently, the operator can switch on or off the threshold for the camera it is enabled for. We can add an option that enables the operator to change the camera the threshold is applied to.

When the topmost GUI option is left clicked multiple times, the GUI options bar randomly turns pink and when left & right clicked outside the GUI options, it turns pink for longer period.

The features of left, right click are present and perform different operations when clicked in different patterns, but these options could become confusing and may overcomplicate the process.

Before the current updated repository version, we had the option of taking pictures using Num 7&8 and video using Num 5&2 but currently we don’t have that option. An option to take picture snapshots and video could be added to fulfill our aim to use those in training before surgery and collecting information.


The Last GUI Option is to go back to the home screen. When right clicked on the last GUI option, it takes us to the home screen where the GUI options bar is minimized. It does not change the GUI features that were already applied.
A bug related to the last GUI option is that, when we left click on it and then left click outside the GUI options (on black screen), then the HMDOpView application crashes.

When the application is run on its current state, without the application of near infrared, white light and segmentation, then it gives few errors, Unhandled request to turn NIR to analog power, Unhandled request to turn white light off. These errors might disappear when we really apply the NIR, white light and segmentation. There is also an error, segmentation fault.

GUI option for selecting a specific area in the video feed is not functional.
There are two options in GUI which have the Exposure option, the second and the third option, but we cannot adjust the exposure using either of the options.

GUI options of Disparity and Register X/Y do not have an adjustment setting in the GUI.

GUI options of Opacity, Calibrate Focus and threshold setting have an adjustment setting in the GUI but cannot be increased or decreased. We could implement it by using a different camera that could do it or build it on the software and GUI.


We have threshold target enabled for one camera, i.e., the USB camera, the other camera displays a regular video. We can change the camera threshold is applied to or enable threshold for both cameras, by making changes in the source code but the need we need segmentation only on one of the camera feeds.

When the threshold is applied, the segmented image frequently is continuously flickering between different colors instead of being stable in a combination of colors. This could be removed by changing the values at which threshold is being applied or by using other methods of applying segmentation. 

We have the option of changing the position of the overlaid camera feeds to a different position if the operator has the preference of moving the position of the overlaid camera feeds to a different position on the display. This can only be done by making changes in the source according to the x and y axis. We could add an option to change the position of the video in the GUI.
