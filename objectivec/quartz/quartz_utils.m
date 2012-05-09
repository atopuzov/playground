#import <Cocoa/Cocoa.h>
#import <Quartz/Quartz.h>
#import <ApplicationServices/ApplicationServices.h>

#import "quartz_utils.h"

int displayBitsPerPixel(CGDisplayModeRef displayMode) {
    // NSLog(@"%@", displayMode);
    int depth = 0;
    if(displayMode != nil) {
        CFStringRef pixelEncoding = CGDisplayModeCopyPixelEncoding(displayMode);
        // modes defined in: IOKit/IOGraphicsTypes.h
        if(CFStringCompare(pixelEncoding, CFSTR(kIO30BitDirectPixels), kCFCompareCaseInsensitive) == kCFCompareEqualTo)
            depth = 30;
        else if(CFStringCompare(pixelEncoding, CFSTR(IO32BitDirectPixels), kCFCompareCaseInsensitive) == kCFCompareEqualTo)
            depth = 32;
        else if(CFStringCompare(pixelEncoding, CFSTR(IO16BitDirectPixels), kCFCompareCaseInsensitive) == kCFCompareEqualTo)
            depth = 16;
        else if(CFStringCompare(pixelEncoding, CFSTR(IO8BitIndexedPixels), kCFCompareCaseInsensitive) == kCFCompareEqualTo)
            depth = 8;
        CFRelease(pixelEncoding);
    }
    return depth;
}
void printDisplayInfo(CGDisplayModeRef displayMode) {
    if(displayMode) {
        // NSLog(@"%@", displayMode);
        int width      = CGDisplayModeGetWidth((CGDisplayModeRef) displayMode);
        int height     = CGDisplayModeGetHeight((CGDisplayModeRef) displayMode);
        int depth      = displayBitsPerPixel((CGDisplayModeRef) displayMode);
        double refresh = CGDisplayModeGetRefreshRate((CGDisplayModeRef) displayMode);
        
        NSLog(@"%dx%dx%d@%.0f", width, height, depth, refresh);
    }
}
void setDisplay(CGDirectDisplayID display, CGDisplayModeRef displayMode) {
    CGDisplayModeRef originalMode = CGDisplayCopyDisplayMode(kCGDirectMainDisplay);
    if (CGDisplaySetDisplayMode(display, displayMode, NULL ) != CGDisplayNoErr) {
        NSLog( @"Could not switch mode!" );
        if (CGDisplaySetDisplayMode(display, originalMode, NULL ) != CGDisplayNoErr) {
            NSLog( @"Could not restore mode!" );
        }
    }
}
CGDisplayModeRef getDisplayMode(int width, int height, int depth) {
    CGDirectDisplayID display = CGMainDisplayID();  // kCGDirectMainDisplay
    
    // Get all available display modes
#if __MAC_OS_X_VERSION_MAX_ALLOWED >= 1060
    NSArray *displayModes = (NSArray *)CGDisplayCopyAllDisplayModes(display, nil);
#else
    NSArray *displayModes = (NSArray *)CGDisplayAvailableModes(display);
#endif
    
    // Loop trough all available display modes
    // Find exact mode
#if __MAC_OS_X_VERSION_MAX_ALLOWED >= 1060
    for(id displayMode in displayModes) {
#else
    for(size_t displayModeCounter = 0; displayModeCounter < [displayModes count]; ++displayModeCounter) {
        id displayMode = [displayModes objectAtIndex:displayModeCounter];
#endif
        //printDisplayInfo((CGDisplayModeRef)displayMode);
        int _width      = CGDisplayModeGetWidth((CGDisplayModeRef) displayMode);
        int _height     = CGDisplayModeGetHeight((CGDisplayModeRef) displayMode);
        int _depth      = displayBitsPerPixel((CGDisplayModeRef) displayMode);
        if ((_width  == width) && (_height == height) && (_depth  == depth)) {
                [displayModes release];
                return (CGDisplayModeRef)displayMode;
            }
    }
    // Find similar mode
#if __MAC_OS_X_VERSION_MAX_ALLOWED >= 1060
    for(id displayMode in displayModes) {
#else
    for(size_t displayModeCounter = 0; displayModeCounter < [displayModes count]; ++displayModeCounter) {
        id displayMode = [displayModes objectAtIndex:displayModeCounter];
#endif
        int _width      = CGDisplayModeGetWidth((CGDisplayModeRef) displayMode);
        int _height     = CGDisplayModeGetHeight((CGDisplayModeRef) displayMode);
        int _depth      = displayBitsPerPixel((CGDisplayModeRef) displayMode);
        if ((_width  >= width) && (_height >= height) && (_depth  == depth)) {
                [displayModes release];
                return (CGDisplayModeRef)displayMode;
        }
    }
    return nil;
}
