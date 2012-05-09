#import <Cocoa/Cocoa.h>
#import <Quartz/Quartz.h>
#import <ApplicationServices/ApplicationServices.h>

#import "AppDelegate.h"
#import "MyWindow.h"
#import "WindowDelegate.h"
#import "MyView.h"

@implementation AppDelegate
- (void) setMenu {
    // Menu bar
    id menuBar     = [[NSMenu new] autorelease];
    id appNameItem = [[NSMenuItem new] autorelease];
    [menuBar addItem:appNameItem];
    
    // First menu
    id appMenu            = [[NSMenu new] autorelease];
    id appAboutItem       = [[[NSMenuItem alloc] initWithTitle: @"About" 
                                                        action: nil
                                                 keyEquivalent: @""] autorelease];
    id appUpdatesItem     = [[[NSMenuItem alloc] initWithTitle: @"Check For Update..."
                                                        action: nil
                                                 keyEquivalent: @""] autorelease];
    id appPreferencesItem = [[[NSMenuItem alloc] initWithTitle: @"Preferences..."
                                                        action: @selector(preferences:)
                                                 keyEquivalent: @","] autorelease];
    id appQuitItem        = [[[NSMenuItem alloc] initWithTitle: @"Quit"
                                                        action: @selector(terminate:)
                                                 keyEquivalent: @"q"] autorelease];
    
    [appMenu addItem: appAboutItem];
    [appMenu addItem: appUpdatesItem];
    [appMenu addItem: [NSMenuItem separatorItem]];
    [appMenu addItem: appPreferencesItem];
    [appMenu addItem: [NSMenuItem separatorItem]];
    [appMenu addItem: appQuitItem];
    [appNameItem setSubmenu:appMenu];
    
    [NSApp setMainMenu:menuBar];
}
- (void) applicationDidFinishLaunching:(NSNotification *)notification {
    // Setup menu
    [self setMenu];
    
    NSRect windowRect = NSMakeRect(0, 0, 800, 600);
    
    window = [[MyWindow alloc] initWithContentRect: windowRect
                                         styleMask: NSClosableWindowMask|NSTitledWindowMask
                                           backing: NSBackingStoreBuffered 
                                             defer: NO];
    [window setTitle:@"My application"];
    [window makeKeyAndOrderFront:nil];
    [window setCollectionBehavior: NSWindowCollectionBehaviorFullScreenPrimary];
    
    windowDelegate = [[WindowDelegate alloc] init];
    [window setDelegate: windowDelegate];
    
    view = [[MyView alloc] initWithFrame: windowRect];
    [window setContentView:view];
    [window makeFirstResponder:view];
}
- (void) applicationWillTerminate:(NSNotification *)notification {
    [window orderOut:self];
    
    if([window inFullScreen]) {
        // NSLog(@"Cleaning up fullscreen state");
        [window tFullScreen];
    }
}
- (void) applicationDidChangeScreenParameters:(NSNotification *)notification {
    // NSLog(@"applicationDidChangeScreenParameters");
}
- (void) dealloc {
    [window release];
    [view release];
    [super dealloc];
}
- (void) applicationWillUnhide:(NSNotification *)notification {
    // NSLog(@"applicationWillUnhide");
    if([window inFullScreen])
    {
        [window makeKeyAndOrderFront:nil];
        [window enterFullScreen];
    }
}
- (void)applicationWillBecomeActive:(NSNotification *)notification {
    NSLog(@"applicationWillBecomeActive");
    if([window inFullScreen])
    {
        [window makeKeyAndOrderFront:nil];
        [window enterFullScreen];
    }
}

@end
