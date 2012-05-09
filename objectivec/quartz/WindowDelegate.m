#import <Cocoa/Cocoa.h>
#import <Quartz/Quartz.h>
#import <ApplicationServices/ApplicationServices.h>

#import "WindowDelegate.h"

@implementation WindowDelegate
- (void)windowDidDeminiaturize:(NSNotification *)notification {
    NSLog(@"WindowDelegate: windowDidDeminiaturize");
}
- (void)windowWillMiniaturize:(NSNotification *)notification {
    NSLog(@"wWindowDelegate: windowWillMiniaturize");
}
- (void)windowWillEnterFullScreen:(NSNotification *)notification {
    // NSLog(@"WindowDelegate: windowWillEnterFullScreen");
    oldTitle = [[notification object] title];
    oldStyleMask = [[notification object] styleMask];
    [[notification object] setStyleMask: NSFullScreenWindowMask];
}
- (void)windowWillExitFullScreen:(NSNotification *)notification {
    // NSLog(@"WindowDelegate: windowWillExitFullScreen");
    [[notification object] setStyleMask: oldStyleMask];
    [[notification object] setTitle: oldTitle];
}
- (NSApplicationPresentationOptions)window:(NSWindow *)window willUseFullScreenPresentationOptions:(NSApplicationPresentationOptions)proposedOptions {
    // NSLog(@"WindowDelegate: window:willUseFullScreenPresentationOptions");
    return NSApplicationPresentationHideDock | NSApplicationPresentationHideMenuBar | NSApplicationPresentationFullScreen;
    // return NSApplicationPresentationHideDock | NSApplicationPresentationAutoHideMenuBar | NSApplicationPresentationFullScreen;
}
@end
