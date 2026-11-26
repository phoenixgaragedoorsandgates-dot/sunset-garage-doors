"""All business facts and page copy live here. Edit this file, then run: python3 _src/build.py"""

SITE = "https://sunsetgaragedoorsmonrovia.com"
BIZ = {
    "name": "Sunset Garage Doors",
    "phone_display": "(626) 606-9766",
    "phone_tel": "+16266069766",
    "street": "507 W Foothill Blvd, Unit B",
    "city": "Monrovia",
    "region": "CA",
    "zip": "91016",
    "lat": 34.1494,
    "lng": -118.0036,
    "license": "1136120",
    "years": 6,
    "google": "https://maps.app.goo.gl/CKL2Y9rbQw3FU8xd6",
    "instagram": "https://www.instagram.com/sunset_garagedoors/",
    "facebook": "https://www.facebook.com/profile.php?id=61593373165234",
    "yelp": "https://www.yelp.com/biz/sunset-garage-doors-monrovia",
    "hours_text": [("Sunday – Thursday", "7:00 AM – 10:00 PM"), ("Friday", "7:00 AM – 5:00 PM"), ("Saturday", "Closed")],
}

BRANDS = ["LiftMaster", "Chamberlain", "CHI Overhead Doors", "Instock Garage Doors", "Elegant Garage Doors"]

CITIES = [
    "Monrovia", "Arcadia", "Duarte", "Bradbury", "Sierra Madre", "Pasadena", "Altadena",
    "South Pasadena", "San Marino", "San Gabriel", "Temple City", "Rosemead", "El Monte",
    "South El Monte", "Alhambra", "Monterey Park", "Irwindale", "Azusa", "Glendora",
    "Baldwin Park", "West Covina", "Covina", "San Dimas", "La Verne", "La Puente",
    "Hacienda Heights", "La Cañada Flintridge", "Glendale",
]

REVIEWS = [
    ("Diana S.", "Opener & spring replacement", "Sunset Garage Doors replaced my garage door opener and spring, and I’m very happy with the results. The door now opens smoothly and quietly. Thank you for the great service! Highly recommend!"),
    ("Tung T.", "Spring repair", "We had issues with our garage door opening and closing. We reached out and Sean came over the next day. He was an absolute professional and was able to explain what was wrong with our springs and ultimately fixed it. Great service!"),
    ("Maria B.", "Spring replacement", "Great experience with Sunset Garage Doors! Our garage door was making loud noises and wasn’t operating properly. The technician identified the problem, replaced the worn-out springs, and made sure everything worked smoothly. Very knowledgeable, honest, and efficient!"),
    ("Jared V.", "Broken spring", "I had an outstanding experience with Sunset Garage Doors. They replaced my broken spring within an hour of calling. Price was right and Moses is very polite and professional. Highly recommended!"),
    ("Yevheniia A.", "Broken spring", "Our garage door spring broke unexpectedly, and Sunset Garage Doors came to the rescue! The technician arrived on time, explained everything clearly, and replaced the broken springs quickly."),
    ("Katerina", "Garage door service", "Sunset Garage Doors did an amazing job! I’m very happy with the service and the results. The team was friendly, professional, and paid attention to every detail. They made the whole process smooth and stress-free."),
]

# Company-wide FAQs (home page + /faq/)
FAQS = [
    ("What areas do you serve?",
     "We're based at 507 W Foothill Blvd in Monrovia and serve homes within about 20 miles, including Arcadia, Duarte, Sierra Madre, Pasadena, Azusa, Glendora, Temple City, San Gabriel, El Monte, West Covina and the rest of the San Gabriel Valley."),
    ("What are your hours?",
     "Sunday through Thursday 7:00 AM to 10:00 PM, Friday 7:00 AM to 5:00 PM. We're closed Saturday."),
    ("Are you licensed?",
     "Yes. Sunset Garage Doors is a licensed California contractor, license #1136120."),
    ("What warranty do you offer?",
     "Every repair comes with a 1-year warranty and every installation comes with a 3-year warranty."),
    ("Do you offer financing?",
     "Yes. We offer financing through Acorn Finance, so you can pay for a new garage door or opener over time. Call us to get started."),
    ("Which brands do you install?",
     "We install and service LiftMaster and Chamberlain openers, and doors from CHI Overhead Doors, Instock Garage Doors and Elegant Garage Doors. We also repair most other brands."),
    ("How do I get a quote?",
     "Call or text (626) 606-9766. Texting a photo or short video of the problem helps us tell you what's likely wrong and bring the right parts."),
    ("Is it safe to fix a garage door spring myself?",
     "We don't recommend it. Garage door springs hold enough tension to lift a door that can weigh a few hundred pounds, and releasing that tension without the right tools can cause serious injury. Leave the door closed and call a technician."),
]

# Services. Each one becomes its own page at /<slug>/
SERVICES = [
    {
        "slug": "garage-door-repair",
        "name": "Garage Door Repair",
        "title": "Garage Door Repair in Monrovia, CA",
        "summary": "Noisy, stuck, slow or crooked doors diagnosed and fixed.",
        "intro": [
            "When your garage door stops working, your car is stuck inside, your house isn't secure and you've got a heavy door you can't trust. Sunset Garage Doors repairs residential garage doors across Monrovia and the San Gabriel Valley.",
            "We find what's actually wrong, explain it clearly, and fix it. Every repair comes with a 1-year warranty.",
        ],
        "signs": [
            "The door won't open or close, or stops partway",
            "Grinding, squeaking, popping or banging noises",
            "The door is crooked, uneven or hanging to one side",
            "It reverses before it touches the ground",
            "It's very heavy to lift by hand",
            "A loud bang came from the garage (usually a broken spring)",
        ],
        "what": "Most repairs involve springs, cables, rollers, hinges, tracks or the opener. We inspect the whole system, not just the part that failed, so you aren't calling again next month for the part next to it.",
        "faqs": [
            ("Why is my garage door making so much noise?", "Common causes are worn rollers, loose hardware, dry moving parts or springs near the end of their life. A tune-up and new nylon rollers often make a door much quieter."),
            ("My door opens a few inches and stops. What's wrong?", "That's often a broken spring or a misadjusted opener force setting. Don't keep running the opener; it can damage the opener and the door. Call or text us a photo."),
        ],
        "image": "door-double-woodgrain",
    },
    {
        "slug": "garage-door-spring-replacement",
        "name": "Spring Replacement",
        "title": "Garage Door Spring Replacement in Monrovia, CA",
        "summary": "Broken torsion and extension springs replaced and balanced.",
        "intro": [
            "A broken spring is the most common garage door repair we do. Springs do the heavy lifting; your opener just guides the door. When one snaps, the door suddenly becomes too heavy to open.",
            "We replace torsion and extension springs, match them to your door's weight, and balance the door so it moves smoothly and your opener isn't strained. Covered by our 1-year repair warranty.",
        ],
        "signs": [
            "You heard a loud bang from the garage",
            "There's a visible gap in the spring above the door",
            "The door opens a few inches, then stops",
            "The door feels extremely heavy by hand",
            "Cables are loose or hanging",
        ],
        "what": "On two-spring doors, we usually recommend replacing both springs at once. They wear at the same rate, so when one breaks, the other is usually close behind. We'll tell you the options and you decide.",
        "faqs": [
            ("Can I open my garage door with a broken spring?", "We don't recommend it. Without the spring, the door's full weight is on you or the opener. Keep the door closed and call us."),
            ("Torsion vs. extension springs: what's the difference?", "Torsion springs mount on a bar above the door and twist to lift it. Extension springs run along the horizontal tracks and stretch. Both store a lot of tension and should be replaced by a technician."),
        ],
        "image": "spring-broken-studio",
        "gallery": [
            ("spring-broken-closeup", "Broken torsion spring with a visible gap in the coils", "Broken torsion spring"),
            ("spring-broken-gap", "Snapped garage door torsion spring on the shaft above the door", "Snapped spring"),
            ("spring-old-removed", "Worn torsion springs and old rollers removed during a spring replacement", "Old springs & rollers removed"),
            ("spring-torsion-studio", "Close-up of a healthy galvanized torsion spring and winding cone", "Healthy torsion spring, close-up"),
            ("spring-torsion-installed", "New torsion spring installed above a garage door", "New torsion spring"),
            ("spring-two-torsion", "Four torsion springs installed on a wood-grain garage door with windows", "Four-spring setup"),
        ],
    },
    {
        "slug": "garage-door-off-track-repair",
        "name": "Off-Track Repair",
        "title": "Garage Door Off-Track Repair in Monrovia, CA",
        "summary": "Doors that jumped the track realigned and secured.",
        "intro": [
            "A door that has come off its track can fall or jam and is dangerous to operate. If your door is crooked, hanging, or the rollers have popped out of the track, stop using it and keep people and cars away.",
            "We put the door back on track, straighten or replace bent track sections, and fix whatever caused it in the first place.",
        ],
        "signs": [
            "Rollers have come out of the track",
            "The door is tilted or hanging on one side",
            "The track is bent or pulled away from the wall",
            "A car or object hit the door",
            "A cable snapped or came off the drum",
        ],
        "what": "Off-track doors are usually caused by a broken cable, a bent track, worn rollers or an impact. We fix the root cause, not just the symptom, so it doesn't happen again.",
        "faqs": [
            ("Can I push my door back on the track myself?", "It's not safe. The door is under spring tension and can shift or fall. Leave it where it is and call us."),
        ],
        "image": "offtrack-collapsed",
        "gallery_title": "What an off-track door looks like",
        "gallery": [
            ("offtrack-collapsed", "Garage door that came off its track and collapsed into the garage", "Door off track and folded in"),
            ("offtrack-bent-panels", "Double garage door with bent, buckled panels after coming off track", "Bent and buckled panels"),
            ("offtrack-crooked-inside", "Inside view of a crooked garage door hanging lower on one side", "Crooked door, inside view"),
        ],
    },
    {
        "slug": "garage-door-opener-repair",
        "name": "Opener Repair",
        "title": "Garage Door Opener Repair in Monrovia, CA",
        "summary": "Openers that hum, reverse or won't respond, repaired.",
        "intro": [
            "If your garage door opener hums but doesn't move, reverses on its own, or ignores the remote, we can find the problem and fix it. We repair LiftMaster, Chamberlain and most other brands.",
            "Opener problems are often caused by misaligned safety sensors, worn gears, travel or force settings, or a door that's out of balance. We check all of it.",
        ],
        "signs": [
            "The opener hums or clicks but the door doesn't move",
            "The door reverses before it closes",
            "The lights on the safety sensors are blinking",
            "Remotes or the wall button work only sometimes",
            "The opener runs but the door doesn't move",
        ],
        "what": "If your opener is old or not worth repairing, we'll tell you honestly and give you a price on a new one, so you can compare.",
        "faqs": [
            ("Why does my garage door go back up when I try to close it?", "Most often the safety sensors near the floor are misaligned, dirty or blocked. It can also be the force settings. If cleaning and lining up the sensors doesn't fix it, call us."),
        ],
        "image": "opener-liftmaster-belt",
        "gallery": [
            ("opener-technician-mounting", "Sunset Garage Doors technician drilling to secure a garage door opener mounting bracket", "Securing the opener bracket"),
            ("opener-liftmaster-belt", "LiftMaster belt-drive garage door opener with built-in LED light", "LiftMaster belt drive"),
            ("opener-liftmaster-led", "LiftMaster myQ garage door opener with LED light on a chain rail", "LiftMaster with LED light"),
            ("opener-liftmaster-chain", "LiftMaster chain-drive opener with emergency release cord", "Chain drive & emergency release"),
            ("opener-liftmaster-camera", "LiftMaster ceiling-mount opener with built-in myQ camera and Wi-Fi", "Opener with myQ camera"),
            ("opener-led-underside", "Garage door opener with LED light ring seen from below", "LED light ring"),
        ],
    },
    {
        "slug": "garage-door-opener-installation",
        "name": "Opener Replacement",
        "title": "Garage Door Opener Installation in Monrovia, CA",
        "summary": "New LiftMaster and Chamberlain openers installed.",
        "intro": [
            "A new opener can make your garage quieter, safer and smarter. We install LiftMaster and Chamberlain openers, including quiet belt-drive models and openers you can control from your phone.",
            "Every opener installation is covered by our 3-year installation warranty.",
        ],
        "signs": [
            "Your opener is loud, slow or unreliable",
            "It's an older unit without modern safety sensors",
            "You want to open and monitor the door from your phone",
            "Repairs would cost close to a new opener",
        ],
        "what": "We remove the old unit, install and program the new opener, set up the safety sensors, adjust travel and force, program your remotes and keypad, and haul away the old opener.",
        "faqs": [
            ("Belt drive or chain drive?", "Belt drives are much quieter, which matters if there's a bedroom above or next to the garage. Chain drives are durable and usually cost less. We'll help you choose."),
        ],
        "image": "opener-liftmaster-led",
        "gallery": [
            ("opener-liftmaster-camera", "New LiftMaster ceiling-mount opener with built-in myQ camera and Wi-Fi", "Ceiling-mount opener with myQ camera"),
            ("opener-led-underside", "New garage door opener with LED light ring, seen from below", "Built-in LED light"),
            ("opener-liftmaster-belt", "New LiftMaster belt-drive opener with built-in LED light", "Quiet belt drive"),
        ],
    },
    {
        "slug": "new-garage-door-installation",
        "name": "New Garage Door Installation",
        "title": "New Garage Door Installation in Monrovia, CA",
        "summary": "New doors in the style and color you want, installed clean.",
        "intro": [
            "A new garage door is one of the most visible upgrades you can make to your home. We install new residential garage doors from CHI Overhead Doors, Instock Garage Doors and Elegant Garage Doors in a range of styles, colors, wood-grain finishes, windows and insulation options.",
            "Every installation is covered by our 3-year warranty, and financing is available through Acorn Finance.",
        ],
        "signs": [
            "Panels are dented, cracked or rotted",
            "The door is old, heavy or not insulated",
            "You want to update the look of your home",
            "Repairs keep adding up",
        ],
        "what": "We help you pick the door, measure, remove and haul away the old door, install the new door with new tracks and springs sized for it, and adjust your opener to match.",
        "faqs": [
            ("Can I get financing on a new garage door?", "Yes, through Acorn Finance. Call us and we'll walk you through it."),
            ("Can you replace my old one-piece door with a sectional door?", "In many garages, yes. We'll look at your opening and tell you what fits."),
        ],
        "image": "newdoor-carriage-hardware",
        "gallery_title": "New doors we've installed",
        "gallery": [
            ("newdoor-full-view-white", "New full-view glass garage door with white aluminum frame", "Full-view glass, white frame"),
            ("newdoor-modern-brown", "New modern flush garage door in brown wood-grain with vertical side windows", "Modern flush, side windows"),
            ("newdoor-modern-black", "New black modern garage door with long side windows", "Modern black"),
            ("newdoor-frosted-inside", "Two new full-view garage doors with frosted glass, seen from inside", "Frosted glass, inside view"),
            ("door-double-woodgrain", "New double garage door with dark wood-grain finish and top windows", "Dark wood-grain, top windows"),
            ("newdoor-carriage-hardware", "New carriage-house garage door with arched windows and black decorative hinges and handles", "Carriage house, decorative hardware"),
            ("newdoor-black-left-windows", "New black wood-grain flush garage door with long windows on the left", "Black flush, left windows"),
            ("newdoor-white-raised-panel", "New white raised-panel garage door with top windows", "Classic white, top windows"),
            ("newdoor-white-flush-arched", "New white flush-panel garage door fitted in an arched opening", "White flush, arched opening"),
            ("newdoor-black-glass-inside", "New black full-view glass garage door seen from inside", "Black glass, inside view"),
        ],
    },
    {
        "slug": "commercial-garage-door-installation",
        "name": "Commercial Garage Doors",
        "title": "Commercial Garage Door Installation in Monrovia, CA",
        "summary": "Steel sectional doors for shops and warehouses in 20, 22 or 24 gauge.",
        "intro": [
            "Sunset Garage Doors installs commercial sectional garage doors for shops, warehouses, auto bays, storage units and other businesses across Monrovia and the San Gabriel Valley.",
            "We offer steel doors in 20, 22 and 24 gauge. The lower the gauge number, the thicker the steel: 20 gauge is the heaviest-duty of the three, and 24 gauge is a lighter, more budget-friendly option. We'll help you choose the right one for how hard the door gets used.",
            "Every installation is covered by our 3-year warranty.",
        ],
        "signs": [
            "Your commercial door is dented, bent or won't seal",
            "You're opening a new shop, warehouse or bay",
            "The door gets heavy daily use and keeps breaking down",
            "You need a sturdier door for security",
            "A space is being remodeled or a new opening was framed",
        ],
        "what": "We measure the opening, help you choose the steel gauge, install the door with tracks, springs and hardware sized for it, and test it before we leave. Ask about openers for commercial doors, too.",
        "faqs": [
            ("What's the difference between 20, 22 and 24 gauge steel?", "Gauge measures steel thickness, and a lower number means thicker steel. 20 gauge is the strongest and most dent-resistant, 22 gauge is a solid middle option, and 24 gauge is lighter and costs less. We'll recommend one based on how the door is used."),
            ("Do you install commercial doors for small businesses?", "Yes. We install doors for shops, garages, warehouses, storage spaces and other businesses throughout the San Gabriel Valley."),
        ],
        "image": "commercial-closed",
        "gallery_title": "Our commercial door work",
        "gallery": [
            ("commercial-open-inside", "New commercial steel sectional door open, seen from inside a warehouse", "Open, from inside"),
            ("commercial-open-side", "Commercial steel garage door tracks and struts seen from inside", "Tracks & struts"),
            ("commercial-opening", "Commercial steel sectional door during installation, with the top panel not yet in place", "During installation"),
        ],
    },
    {
        "slug": "one-piece-garage-doors",
        "name": "One-Piece Doors",
        "title": "One-Piece Garage Door Repair & Installation in Monrovia, CA",
        "summary": "Tilt-up door repair, new installs, and doors custom-built on site.",
        "intro": [
            "Many older homes in the San Gabriel Valley still have one-piece (tilt-up) garage doors that swing out as a single panel. They use different springs, hardware and arms than sectional doors, and not every company works on them. We do.",
            "We repair one-piece doors and install new ones. Because one-piece openings come in all sizes, we also custom-build one-piece doors right on site, framed to fit your exact opening. If you'd rather switch to a sectional door, we can tell you whether your opening allows it.",
        ],
        "signs": [
            "The door is very heavy or won't stay open",
            "Springs or arms are broken or bent",
            "The door sags or drags on the ground",
            "The wood is cracked, warped or rotting",
        ],
        "what": "Repairs are covered for 1 year and new installations for 3 years.",
        "faqs": [
            ("Can you build a one-piece door to fit my opening?", "Yes. We custom-make one-piece doors on site, building the frame to the exact size of your garage opening, then install it with new arms and springs."),
            ("Are one-piece doors still worth repairing?", "Often, yes. Springs and hardware can usually be replaced. If the door itself is rotted or warped, replacement usually makes more sense, and we'll give you both options."),
        ],
        "image": "onepiece-open-outside",
        "gallery": [
            ("onepiece-custom-build", "One-piece garage door being custom-built on site with a steel frame and window panels", "Custom-built on site"),
            ("onepiece-carriage-inside", "New carriage-style one-piece garage door with windows, arms and springs on both sides, seen from inside", "Carriage-style door, inside view"),
            ("onepiece-open-inside", "One-piece garage door fully open, seen from inside the garage", "Open, from inside"),
            ("onepiece-springs", "New pair of one-piece garage door extension springs installed", "New springs"),
            ("onepiece-technician", "Sunset Garage Doors technician adjusting one-piece door hardware", "Adjusting the hardware"),
        ],
    },
    {
        "slug": "garage-door-roller-hinge-replacement",
        "name": "Rollers & Hinges",
        "title": "Garage Door Roller & Hinge Replacement in Monrovia, CA",
        "summary": "Worn rollers and cracked hinges replaced for a smooth, quiet door.",
        "intro": [
            "Rollers and hinges move every time your door does. When they wear out, the door gets noisy, shaky and harder on your opener. A cracked hinge can also damage your door panels.",
            "We replace worn rollers with smooth, quiet nylon rollers and swap out cracked or bent hinges. Covered by our 1-year repair warranty.",
        ],
        "signs": [
            "Grinding or rattling as the door moves",
            "Rollers that wobble, are chipped, or don't spin",
            "Cracked, bent or loose hinges",
            "The door shakes or jerks while moving",
        ],
        "what": "We usually replace all rollers at once and check every hinge, so the door runs evenly.",
        "faqs": [
            ("Will new rollers make my door quieter?", "Usually, yes. Swapping old steel rollers for nylon ones is one of the easiest ways to quiet a noisy door."),
        ],
        "image": "hinge-roller-closeup",
        "gallery": [
            ("hinge-roller-closeup", "Heavy-duty 14-gauge garage door hinge with a nylon roller in the track", "14-gauge hinge & nylon roller"),
            ("roller-old-vs-new", "New white nylon garage door roller next to a worn black roller", "New nylon roller vs. worn old roller"),
            ("hinge-roller-track", "Garage door hinge and nylon roller riding in the side track", "Hinge & roller in the track"),
        ],
    },
    {
        "slug": "garage-door-cable-drum-repair",
        "name": "Cables & Drums",
        "title": "Garage Door Cable & Drum Repair in Monrovia, CA",
        "summary": "Frayed or snapped lift cables and worn drums replaced.",
        "intro": [
            "Lift cables run from the bottom of your garage door up to the drums on the spring shaft. Together with the springs, they raise and lower the door evenly. When a cable frays, snaps or slips off its drum, the door can hang crooked, jam or come off track.",
            "We replace worn or broken cables and drums, re-seat cables on the drums and balance the door so both sides lift evenly. Covered by our 1-year repair warranty.",
        ],
        "signs": [
            "A cable is frayed, rusty or has broken strands",
            "A cable is loose, hanging or has come off the drum",
            "The door is crooked or one side is lower than the other",
            "The door jerks or makes a snapping sound",
            "A spring recently broke (cables often get damaged too)",
        ],
        "what": "Cables are under a lot of tension from the springs. Don't try to re-thread or replace them yourself. Keep the door closed and call us.",
        "faqs": [
            ("Why did my garage door cable come off the drum?", "Common causes are a broken spring, a door that hit something while closing, worn cables, or the door being pulled down unevenly. We re-seat or replace the cable and fix whatever caused it."),
            ("Should both cables be replaced at once?", "Usually, yes. Both cables wear at the same rate, so if one is frayed or broken, the other is often close behind."),
        ],
        "image": "cable-drum",
        "gallery_title": "Cables & drums",
        "gallery": [
            ("cable-frayed", "Snapped and frayed garage door lift cable", "Snapped, frayed cable"),
        ],
    },
    {
        "slug": "garage-door-reinforcement",
        "name": "Door Reinforcement",
        "title": "Garage Door Reinforcement & Struts in Monrovia, CA",
        "summary": "Garage door struts that straighten and strengthen bent, sagging panels.",
        "intro": [
            "Wide doors and lightweight panels can bend, bow or sag over time, especially the top section where the opener pulls. A cracked or bent panel also weakens the whole door.",
            "The fix is a garage door strut: a long steel brace bolted across the inside of a panel. Struts reinforce bent doors, keep sections straight, and stop the damage from getting worse.",
            "We install struts on the sections that need them and check the rest of the door while we're there.",
        ],
        "signs": [
            "A panel is bent, buckled or cracked",
            "The top panel is bending where the opener arm attaches",
            "Panels sag in the middle",
            "The door flexes or bows when it moves",
            "You added a heavier opener or windows",
        ],
        "what": "Adding struts is a small job that can add years to a door's life, and it often costs far less than replacing a panel or the whole door.",
        "faqs": [
            ("What is a garage door strut?", "A strut is a steel brace that bolts horizontally across the inside of a garage door section. It reinforces the panel so it can't bend or sag, and it's used to strengthen doors that are already bent."),
            ("Why is the top of my garage door bending?", "The opener pulls on the top section every time the door moves. Without a strut, that section can bend over time. A reinforcement strut fixes it."),
            ("Can a bent garage door panel be fixed with a strut?", "Often, yes. If the panel is bent but not torn apart, a strut can straighten and reinforce it. If the panel is badly cracked or split, it may need to be replaced, and we'll tell you which makes sense."),
        ],
        "image": "reinforcement-bent-panel",
    },
    {
        "slug": "garage-door-remotes-keypads",
        "name": "Remotes & Keypads",
        "title": "Garage Door Remotes & Keypads in Monrovia, CA",
        "summary": "New remotes and keypads programmed to your opener.",
        "intro": [
            "Lost a remote, moved into a new home, or want a keypad so the kids can get in? We supply and program remotes and wireless keypads for LiftMaster, Chamberlain and many other openers.",
            "If your opener is too old to work with modern remotes, we'll tell you your options.",
        ],
        "signs": [
            "You lost a remote or just moved in",
            "Remotes only work up close",
            "You want a keypad outside the garage",
            "You want to open the door from your phone",
        ],
        "what": "We can usually add remotes and keypads during any other service visit.",
        "faqs": [
            ("Should I reprogram my opener after moving into a new home?", "Yes. The previous owners may still have remotes. We can clear the old codes and program new remotes for you."),
        ],
        "image": "door-single-woodgrain",
    },
]

# Display order of services (edit this list to reorder everywhere on the site)
SERVICE_ORDER = [
    "garage-door-repair",
    "garage-door-spring-replacement",
    "garage-door-opener-repair",
    "garage-door-off-track-repair",
    "new-garage-door-installation",
    "garage-door-cable-drum-repair",
    "garage-door-opener-installation",
    "garage-door-roller-hinge-replacement",
    "commercial-garage-door-installation",
    "one-piece-garage-doors",
    "garage-door-reinforcement",
    "garage-door-remotes-keypads",
]
assert sorted(SERVICE_ORDER) == sorted(x["slug"] for x in SERVICES)
SERVICES.sort(key=lambda x: SERVICE_ORDER.index(x["slug"]))

GALLERY = [
    ("door-double-woodgrain", "Double garage door, dark wood-grain finish with top windows", "2-Car Garage Door Installation"),
    ("door-single-woodgrain", "Single garage door, dark wood-grain finish with windows", "1-Car Garage Door Installation"),
    ("technician-installing", "Technician fastening weather seal above a new garage door", "Weather Seal"),
]
