#import <Cocoa/Cocoa.h>
#import <Quartz/Quartz.h>
#import <ApplicationServices/ApplicationServices.h>

#import "MyApp.h"
#import "MyWindow.h"

@implementation MyApp
- (void) sendEvent:(NSEvent *)event {
    // NSLog(@"MyApp: sendEvent");
    NSEventType type = [event type];
    BOOL done = NO;

    if(type == NSKeyDown) {
        unichar chr = [[event characters] characterAtIndex:0];
        NSUInteger modifierFlags = [event modifierFlags];
        
        if( chr == '\033' || chr == 'q') {
            // NSLog(@"Terminate");
            [self terminate:nil];
            done = YES;
        }
        else if( chr == 'f') {
            // NSLog(@"Fullscreen");
            [(MyWindow *)[self mainWindow] tFullScreen];
            done = YES;
        }
        else if( chr == 'm') {
            // NSLog(@"Minimize");
            [[self mainWindow] miniaturize:nil];
            done = YES;
        }
        else if( chr == 'h') {
            // NSLog(@"Hide");
            [self hide:nil];
            done = YES;
        }
        else if(chr == 'p') {
            [[self mainWindow] toggleFullScreen:nil];
            done = YES;
        }
        else if((chr == '\t') && (modifierFlags & NSCommandKeyMask)) {
            // NSLog(@"Cmd+Tab");
            if([(MyWindow *)[self mainWindow] inFullScreen]) {
                // [[self mainWindow] orderOut:self]; 
                [(MyWindow *)[self mainWindow] exitFullScreen];
                [self hide:nil];
                done = YES;
            }
            // [self miniaturize:nil];
            // [self hide:nil];
        }
    }
    if(!done)
        [super sendEvent: event];
}
@end
