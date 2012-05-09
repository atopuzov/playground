#import <Cocoa/Cocoa.h>
#import <Quartz/Quartz.h>
#import <ApplicationServices/ApplicationServices.h>

int displayBitsPerPixel(CGDisplayModeRef displayMode);
void printDisplayInfo(CGDisplayModeRef displayMode);
void setDisplay(CGDirectDisplayID display, CGDisplayModeRef displayMode);
CGDisplayModeRef getDisplayMode(int width, int height, int depth);
