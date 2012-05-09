#import <Cocoa/Cocoa.h>
#import <Quartz/Quartz.h>
#import <ApplicationServices/ApplicationServices.h>

#import "MyWindow.h"
#import "MyView.h"
#import "quartz_utils.h"

@implementation MyWindow
@synthesize inFullScreen;
- (void) dealloc {
    CGDisplayModeRelease(savedMode);
    [oldWindowTitle release];
    [super dealloc];
}
- (BOOL) canBecomeKeyWindow {
    return YES;
}
- (BOOL) canBecomeMainWindow {
    return YES;
}
- (void) fadeIn {
    if(CGAcquireDisplayFadeReservation(kCGMaxDisplayReservationInterval, &fadeToken) == kCGErrorSuccess) {
        CGDisplayFade(fadeToken,0.5, kCGDisplayBlendNormal, kCGDisplayBlendSolidColor, 0, 0, 0, TRUE);
    }
    CGReleaseDisplayFadeReservation(fadeToken);
}
- (void) fadeOut {
    if(CGAcquireDisplayFadeReservation(kCGMaxDisplayReservationInterval, &fadeToken) == kCGErrorSuccess) {
        CGDisplayFade(fadeToken, 0.3, kCGDisplayBlendNormal, kCGDisplayBlendSolidColor, 0, 0, 0, TRUE);
    }
    CGReleaseDisplayFadeReservation(fadeToken);
}
- (void) enterFullScreen {
    // Save current mode
    savedMode = CGDisplayCopyDisplayMode(kCGDirectMainDisplay);
    // printDisplayInfo(savedMode);
    
    [self fadeIn];
    
    // Capture main display
    if (CGDisplayCapture( kCGDirectMainDisplay ) != kCGErrorSuccess) {
        NSLog( @"Could not capture the main display!" );
        [NSApp terminate: nil];
    }
    
    CGDisplayModeRef desiredMode = getDisplayMode(800,600,32);
    // printDisplayInfo(desiredMode);
    
    setDisplay(kCGDirectMainDisplay, desiredMode);
    
    int windowLevel = CGShieldingWindowLevel();
    oldWindowLevel = [self level];
    oldWindowStyleMask = [self styleMask];
    oldWindowTitle = [self title];
    [self setLevel:windowLevel];
    [self setStyleMask:NSBorderlessWindowMask];
    [self setFrame:[[self screen] frame] display:YES];
    
    // Enter fullscreen
    // NSDictionary *options = [NSDictionary dictionaryWithObjectsAndKeys:[NSNumber numberWithBool:NO], NSFullScreenModeAllScreens, nil];
    // [[self contentView] enterFullScreenMode:[self screen] withOptions:options];
    
    // [self toggleFullScreen:nil];
}
- (void) exitFullScreen {
    [self fadeOut];
    setDisplay(kCGDirectMainDisplay, savedMode);
    
    // Release the display(s)
    if (CGDisplayRelease( kCGDirectMainDisplay ) != kCGErrorSuccess) {
        NSLog( @"Could not release the display!" );
    }
    // Exit from fullscreen
    
    // Top window
    [self setLevel:oldWindowLevel];
    [self setStyleMask:oldWindowStyleMask];
    [self setTitle:oldWindowTitle];
    
    // NSView 10.5+
    // [[self contentView] exitFullScreenModeWithOptions:nil];
    
    // Use Lion fullscreen mode, 10.7+
    // [self toggleFullScreen:nil];
}
- (void) tFullScreen {
    if([self inFullScreen]) {
        [self setInFullScreen:NO];
        [self exitFullScreen];
    } else {
        [self enterFullScreen];
        [self setInFullScreen:YES];
    }    
}
- (id)initWithContentRect:(NSRect)contentRect styleMask:(NSUInteger)windowStyle backing:(NSBackingStoreType)bufferingType defer:(BOOL)deferCreation {
    self = [super initWithContentRect:contentRect
                            styleMask:windowStyle
                              backing:bufferingType
                                defer:(BOOL)deferCreation];
    if(self)
    {
        [self setInFullScreen:FALSE];
    }
    return self;
}
@end
