#import <Cocoa/Cocoa.h>
#import <Quartz/Quartz.h>
#import <ApplicationServices/ApplicationServices.h>

@interface MyWindow : NSWindow {
    BOOL inFullScreen;
    NSUInteger oldWindowLevel;
    NSUInteger oldWindowStyleMask;
    NSString *oldWindowTitle;
    CGDisplayModeRef savedMode;
    CGDisplayFadeReservationToken fadeToken;
}
@property BOOL inFullScreen;
- (void) enterFullScreen;
- (void) exitFullScreen;
- (void) tFullScreen;
@end
