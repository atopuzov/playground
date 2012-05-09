#import <Cocoa/Cocoa.h>
#import <Quartz/Quartz.h>
#import <ApplicationServices/ApplicationServices.h>

#import "MyView.h"

@implementation MyView
- (id) init {
    // NSLog(@"MyView: init");
    if(self = [super init]) {
        image  = [[NSImage alloc] initWithContentsOfFile:@"icon.tiff"];
        points = [[NSMutableArray alloc] init];
        // [self setIsCommandPressed:NO];
        // [self setIsOptionPressed:NO];
        // [self setIsShiftPressed:NO];
        // [self setIsControlPressed:NO];
    }
    return self;
}
- (id) initWithFrame:(NSRect)rect {
    // NSLog(@"MyView: initWithFrame");
    if(self = [super initWithFrame: rect]) {
        image  = [[NSImage alloc] initWithContentsOfFile:@"icon.tiff"];
        points = [[NSMutableArray alloc] init];
    }
    return self;
}
- (void) dealloc {
    [image release];
    [points release];
    [super dealloc];
}
- (void) mouseDown:(NSEvent*)event {
    // NSLog(@"MyView mouseDown");
    NSPoint tMousePointInWindow = [event locationInWindow];
    NSPoint tMousePointInView   = [self convertPoint:tMousePointInWindow fromView:nil];
    // NSLog(@"%f, %f", tMousePointInView.x, tMousePointInView.y);
    [points addObject:[NSValue valueWithPoint:tMousePointInView]];
    [self setNeedsDisplay:YES];
    // [super mouseDown:event];
}
- (void) drawRect:(NSRect)rect {
    // NSLog(@"MyView: drawRect");
    for(id point in points) {
        NSPoint p = [point pointValue];
        NSRect destRect = NSMakeRect(p.x, p.y, 20, 20);
        [image drawInRect: destRect
                 fromRect: NSZeroRect
                operation: NSCompositeSourceOver
                 fraction: 1.0];
    }
}
- (BOOL) acceptsFirstResponder {
    return YES;
}
@end
