#import <Cocoa/Cocoa.h>
#import <Quartz/Quartz.h>
#import <ApplicationServices/ApplicationServices.h>


@interface AppDelegate : NSObject < NSApplicationDelegate >
{
    id window;
    id windowDelegate;
    id view;
}
- (void) setMenu;
@end
