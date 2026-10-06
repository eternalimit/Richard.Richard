# MOXY Toy Platform
## Cost Reset and Product Pivot

Status: ACTIVE DESIGN DIRECTION

### Decision

BOXY v5 is preserved as a long-term reference concept, but it is too expensive for the first product.

MOXY will now prioritize a low-cost intelligent toy platform designed for simple assembly, low part count, safe operation, easy repair, and mass production.

### Product Goal

Create a small character robot that delivers the core MOXY experience without the cost of a full mobile humanoid.

Target characteristics:

- tabletop or floor toy scale
- expressive screen face
- microphone and speaker
- simple camera optional by model
- Wi-Fi / Bluetooth
- low-cost embedded compute
- simple head motion
- simple arm motion
- wheels or fixed base depending on version
- USB-C charging
- molded plastic shell
- standardized screws and connectors
- modular electronics board
- no high-force joints
- no heavy payload requirement
- no expensive LiDAR requirement
- no industrial drivetrain
- no complex autonomous manipulation

### Cost Strategy

Design around commodity parts, injection-moldable shells, a small number of motors, one main PCB, one battery pack, and minimal wiring.

Initial product targets:

- Toy BOM target: under $100
- Stretch BOM target: under $75
- Retail target: approximately $199-$299
- Assembly target: under 20 minutes at scale
- Primary build method: snap-fit + standard fasteners + prebuilt electronic modules

These are design targets, not validated production costs.

### Minimum Product Architecture

FACE / DISPLAY
-> microphone
-> speaker
-> optional camera

MAIN PCB
-> embedded processor
-> wireless
-> motor control
-> audio
-> power management

MOTION
-> head servo
-> two simple arm servos
-> optional two-wheel drive

POWER
-> rechargeable battery
-> BMS / protection
-> USB-C charge input

SOFTWARE
-> character behavior
-> voice interaction
-> simple games
-> parental / administrator controls
-> firmware update
-> optional cloud AI

### Product Principle

Keep the intelligence high and the hardware simple.

The first MOXY Toy should win through personality, conversation, learning, character behavior, and software rather than expensive mechanical complexity.

### Production Direction

RECEIVE PARTS
-> KIT
-> PCB + BATTERY
-> SHELL
-> MOTORS
-> FACE / DISPLAY
-> FINAL ASSEMBLY
-> FLASH SOFTWARE
-> FUNCTION TEST
-> PACK

### TCGE State

Reality: BOXY v5 is an existing concept in the current project history.
Inference: a simplified toy platform should materially reduce cost and manufacturing complexity.
Echo: independent supplier quotations, prototype BOM, assembly-time study, safety testing, and pilot production have not yet been completed.

Result: GROUNDED INFERENCE / HOLD on validated production cost.

### Continuation Point

Next block: MOXY TOY v1 - minimum viable intelligent character robot.
