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
        "image": "technician-installing",
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
        "image": "door-double-woodgrain",
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
        "image": "door-single-woodgrain",
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
        "image": "door-double-woodgrain",
    },
    {
        "slug": "one-piece-garage-doors",
        "name": "One-Piece Doors",
        "title": "One-Piece Garage Door Repair & Installation in Monrovia, CA",
        "summary": "Tilt-up door repair and new one-piece door installation.",
        "intro": [
            "Many older homes in the San Gabriel Valley still have one-piece (tilt-up) garage doors that swing out as a single panel. They use different springs, hardware and arms than sectional doors, and not every company works on them. We do.",
            "We repair one-piece doors and install new ones. If you'd rather switch to a sectional door, we can tell you whether your opening allows it.",
        ],
        "signs": [
            "The door is very heavy or won't stay open",
            "Springs or arms are broken or bent",
            "The door sags or drags on the ground",
            "The wood is cracked, warped or rotting",
        ],
        "what": "Repairs are covered for 1 year and new installations for 3 years.",
        "faqs": [
            ("Are one-piece doors still worth repairing?", "Often, yes. Springs and hardware can usually be replaced. If the door itself is rotted or warped, replacement usually makes more sense, and we'll give you both options."),
        ],
        "image": "onepiece-open-outside",
        "gallery": [
            ("onepiece-open-inside", "One-piece garage door fully open, seen from inside the garage", "Open, from inside"),
            ("onepiece-hardware", "New one-piece garage door arms, bracket and extension springs", "Arms & springs"),
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
        ],
    },
    {
        "slug": "garage-door-reinforcement",
        "name": "Door Reinforcement",
        "title": "Garage Door Reinforcement in Monrovia, CA",
        "summary": "Struts and bracing that stop sagging and protect your door.",
        "intro": [
            "Wide doors and lightweight panels can bow or sag over time, especially the top section where the opener pulls. Reinforcement struts add strength so the door stays straight.",
            "We install struts and bracing on the sections that need it and check the rest of the door while we're there.",
        ],
        "signs": [
            "The top panel is bending where the opener arm attaches",
            "Panels sag in the middle",
            "The door flexes or bows when it moves",
            "You added a heavier opener or windows",
        ],
        "what": "Reinforcement is a small job that can add years to a door's life.",
        "faqs": [
            ("Why is the top of my garage door bending?", "The opener pulls on the top section every time the door moves. Without a strut, that section can bend over time. A reinforcement strut fixes it."),
        ],
        "image": "technician-installing",
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

GALLERY = [
    ("door-double-woodgrain", "Double garage door, dark wood-grain finish with top windows", "Double Door Installation"),
    ("door-single-woodgrain", "Single garage door, dark wood-grain finish with windows", "Single Door Installation"),
    ("technician-installing", "Technician fastening weather seal above a new garage door", "Weather Seal"),
]
