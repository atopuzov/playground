#import <Cocoa/Cocoa.h>
#import <Quartz/Quartz.h>
#import <ApplicationServices/ApplicationServices.h>


@interface WindowDelegate : NSObject <NSWindowDelegate>  {
    NSUInteger oldStyleMask;
    NSString *oldTitle;
}
@end
