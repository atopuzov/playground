#import <Cocoa/Cocoa.h>
#import <Quartz/Quartz.h>
#import <ApplicationServices/ApplicationServices.h>

#import "AppDelegate.h"
#import "MyApp.h"

int main(int argc, char *argv[]) {
    [NSAutoreleasePool new];
    id app = [[MyApp new] autorelease];
    // id app = [NSApplication sharedApplication];
    
    // Display menu
    [app setActivationPolicy:NSApplicationActivationPolicyRegular];
    
    id appDelegate = [[AppDelegate new] autorelease];
    [app setDelegate:appDelegate];
    [app activateIgnoringOtherApps:YES];
    [app run];
    
    return EXIT_SUCCESS;
}
