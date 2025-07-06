import random
import time
import sys
from datetime import datetime, timedelta

# Color codes
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

def typewriter(text, speed=0.03, color=""):
    color_code = getattr(Colors, color.upper(), "")
    print(color_code, end="")
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print(Colors.RESET, end="")

# Define suspects, locations, and crimes
suspects = {
    "Alice Kaminski": {
        "occupation": "Forensic Artist",
        "age": 37,
        "traits": ["observant", "perfectionist"],
        "common_alibi": ["was sketching a composite", "attending an art exhibit"],
        "weaknesses": ["financially overextended", "obsessed with cold cases"]
    },
    "Robert Vance": {
        "occupation": "Security Consultant",
        "age": 44,
        "traits": ["meticulous", "paranoid"],
        "common_alibi": ["conducting a security audit", "testing alarm systems"],
        "weaknesses": ["gambling debts", "hacked systems before"]
    },
    "Charles Lin": {
        "occupation": "Toxicologist",
        "age": 39,
        "traits": ["precise", "curious"],
        "common_alibi": ["analyzing lab samples", "teaching a workshop"],
        "weaknesses": ["access to restricted chemicals", "research fraud allegation"] 
    },
    "Diana Monroe": {
        "occupation": "Private Investigator",
        "age": 47,
        "traits": ["skeptical", "resourceful"],
        "common_alibi": ["on surveillance duty", "interviewing witnesses"],
        "weaknesses": ["blackmails clients", "planted evidence before"]
    },
    "Evan Petrov": {
        "occupation": "Cybersecurity Analyst",
        "age": 33, 
        "traits": ["analytical", "secretive"],
        "common_alibi": ["patching systems", "at a hacker convention"],
        "weaknesses": ["dark web connections", "created malware previously"]
    },
    "Fiona Zhao": {
        "occupation": "Art Conservator",
        "age": 29,
        "traits": ["patient", "detail-oriented"],
        "common_alibi": ["restoring a painting", "authenticating artifacts"],
        "weaknesses": ["art forgery skills", "sold fakes before"]
    },
    "Gregory Stone": {
        "occupation": "Insurance Investigator",
        "age": 51,
        "traits": ["suspicious", "thorough"],
        "common_alibi": ["processing a claim", "inspecting damage"],
        "weaknesses": ["takes bribes", "orchestrated frauds"]
    },
    "Hannah Wright": {
        "occupation": "Crime Scene Cleaner",
        "age": 34,
        "traits": ["stoic", "efficient"],
        "common_alibi": ["on a cleaning job", "disposing biohazards"],
        "weaknesses": ["knows evidence disposal", "takes souvenirs"]
    }
}

locations = {
    "City Museum of Art": {
        "items": ["Van Gogh painting", "Renaissance sculpture", "ancient manuscript"],
        "clues": ["broken motion sensors", "paint flecks matching restoration tools", "deactivated alarms during maintenance"],
        "security": ["laser grid", "thermal cameras", "night guards"]
    },
    "First National Bank": {
        "items": ["safety deposit contents", "rare coins", "uncut diamonds"],
        "clues": ["vault timer discrepancy", "blueprint copies found", "security uniforms missing"],
        "security": ["mantrap entrance", "dye packs", "armed response team"]
    },
    "TechStart Inc": {
        "items": ["AI source code", "quantum chip designs", "user database"],
        "clues": ["backdoor in logs", "VPN anomalies", "stolen security badges"],
        "security": ["biometric locks", "air-gapped servers", "military encryption"]
    },
    "Blackwood Manor": {
        "items": ["family jewels", "secret will", "rare books"],
        "clues": ["disturbed dust patterns", "replaced locks", "servant testimony conflicts"],
        "security": ["guard dogs", "panic rooms", "motion lights"]
    },
    "Mercy Hospital": {
        "items": ["experimental drug", "patient records", "research data"],
        "clues": ["falsified logs", "tampered cameras", "unauthorized access"],
        "security": ["keycard access", "controlled substances lockup", "24/7 staff"]
    }
}

crimes = [
    ("stole the", ["classified documents", "prototype device", "valuable artifact"], "theft"),
    ("tampered with", ["evidence", "security footage", "financial records"], "tampering"),
    ("forged the", ["will", "painting", "signature"], "forgery"),
    ("hacked into the", ["database", "surveillance system", "encrypted files"], "cybercrime"),
    ("planted", ["fake evidence", "listening devices", "malware"], "deception"),
    ("blackmailed using", ["compromising photos", "stolen data", "fabricated evidence"], "extortion")
]

def generate_case_id():
    chars = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"
    return ''.join(random.choices(chars, k=6))

def generate_mystery():
    culprit_name = random.choice(list(suspects.keys()))
    culprit = suspects[culprit_name]
    location_name = random.choice(list(locations.keys()))
    crime_type, crime_items, crime_category = random.choice(crimes)
    crime_item = random.choice(crime_items)
    
    crime_time = f"{random.randint(18,23):02d}:{random.randint(0,59):02d}"
    case_id = generate_case_id()
    difficulty = random.choice(["Standard", "Complex", "Baffling"])
    
    #Suspect selection
    other_suspects = [s for s in suspects.keys() if s != culprit_name]
    shown_suspects = random.sample(other_suspects, 3) + [culprit_name]
    random.shuffle(shown_suspects)
    
    #Clue generation
    true_clues = [
        f"Forensic traces match {culprit['occupation']} tools",
        f"{culprit_name} had means and opportunity",
        f"Behavioral analysis shows {culprit['traits'][0]} patterns",
        f"Digital footprint places {culprit_name} at scene"
    ]
    
    false_clues = []
    for s in [s for s in shown_suspects if s != culprit_name]:
        s_data = suspects[s]
        false_clues.extend([
            f"{s} has motive: {s_data['weaknesses'][0]}",
            f"Witness saw {s} near scene",
            f"{s_data['occupation']} tools found nearby",
            f"{s} lied about alibi"
        ])
    
    total_clues = min(6, 2 + len(false_clues))
    clues = [random.choice(true_clues)] + random.sample(false_clues, total_clues-1)
    random.shuffle(clues)
    
    return {
        "case_id": case_id,
        "culprit": culprit_name,
        "culprit_profile": culprit,
        "crime": f"{crime_type} {crime_item}",
        "category": crime_category,
        "location": location_name,
        "time": crime_time,
        "difficulty": difficulty,
        "suspects": shown_suspects,
        "clues": clues,
        "motive": f"{culprit['weaknesses'][0]} and {culprit['traits'][1]} nature"
    }

def display_case_narrative(case):
    typewriter("\n" + "="*50, color="yellow")
    typewriter(f"\nCASE FILE #{case['case_id']}", speed=0.05, color="bold")
    typewriter(f"Classification: {case['difficulty']} {case['category'].upper()}", color="cyan")
    
    #Narrative
    narrative = [
        f"\nOn {random.choice(['Tuesday','Wednesday','Friday'])} evening at approximately {case['time']}, ",
        f"security at the {case['location']} reported a {case['category']}. ",
        f"The criminal {case['crime']}, exploiting {random.choice(locations[case['location']]['clues'])}. ",
        "\n\nPotential suspects connected to the case:\n"
    ]
    
    for suspect in case['suspects']:
        s_data = suspects[suspect]
        narrative.append(
            f"- {suspect}, {s_data['age']}, {s_data['occupation']}. " +
            f"Known to be {s_data['traits'][0]} with {s_data['traits'][1]} tendencies. " +
            f"Claims they were {random.choice(s_data['common_alibi'])}.\n"
        )
    
    # Evidence
    narrative.append("\nKey investigative findings:\n")
    for i, clue in enumerate(case['clues'], 1):
        narrative.append(f"{i}. {clue}\n")
    
    narrative.append("\nAdditional notes: Some evidence may be misleading. Cross-reference carefully.\n")
    
    typewriter("".join(narrative))

def get_player_guess(case):
    while True:
        try:
            choice = input(f"\nEnter suspect number (1-4): ")
            choice = int(choice)
            if 1 <= choice <= 4:
                return case['suspects'][choice-1]
            raise ValueError
        except ValueError:
            typewriter("Please enter number 1-4", color="red")

def reveal_solution(case, correct):
    typewriter("\n" + "="*50, color="yellow")
    typewriter("\nCASE RESOLUTION", speed=0.05, color="bold")
    
    culprit = suspects[case['culprit']]
    
    if correct:
        typewriter("\nYour deduction was correct.", color="green")
    else:
        typewriter("\nYour conclusion missed the mark.", color="red")
    
    typewriter(f"\nThe perpetrator was {case['culprit']}, the {culprit['occupation'].lower()}.", color="bold")
    typewriter(f"\nProfile: {culprit['age']}-year-old with history of {culprit['traits'][0]} behavior.")
    typewriter(f"Motive: {case['motive']} led to this {case['category']}.")
    
    method = random.choice([
        f"Used {culprit['occupation'].lower()} knowledge to bypass security",
        f"Exploited access privileges during {random.choice(['maintenance','audit','inspection'])}",
        f"Created false trails pointing to others"
    ])
    typewriter(f"\nMethod: {method}")
    
    evidence = random.choice([
        "DNA under victim's fingernails",
        "Digital forensics uncovered hidden files",
        "Financial records show suspicious payments",
        "Tool marks match professional equipment"
    ])
    typewriter(f"\nKey evidence: {evidence}")

def play_round():
    case = generate_mystery()
    display_case_narrative(case)
    
    start = time.time()
    guess = get_player_guess(case)
    solve_time = int(time.time() - start)
    
    correct = guess == case['culprit']
    reveal_solution(case, correct)
    
    return {
        "correct": correct,
        "time": solve_time,
        "case_id": case['case_id'],
        "difficulty": case['difficulty']
    }

def main():
    typewriter("\nFORENSIC INVESTIGATION SIMULATOR", speed=0.07, color="header")
    typewriter("\nSolve three complex cases using deductive reasoning.", color="blue")
    input("Press Enter to begin your investigation...")
    
    results = []
    for i in range(1,4):
        typewriter(f"\nCASE {i}: INITIALIZING INVESTIGATION", color="bold")
        results.append(play_round())
        if i < 3:
            input("\nPress Enter to continue to next case...")
    
    # Result
    solved = sum(1 for r in results if r['correct'])
    avg_time = sum(r['time'] for r in results)/len(results)
    
    typewriter("\n" + "="*50, color="yellow")
    typewriter("\nINVESTIGATION SUMMARY", speed=0.05, color="bold")
    typewriter(f"\nCases solved: {solved}/3", color="cyan")
    typewriter(f"Average solve time: {avg_time:.1f} seconds", color="cyan")
    
    if solved == 3:
        typewriter("\nPerfect record! You should lead the next major investigation.", color="green")
    elif solved >= 2:
        typewriter("\nSolid performance. Ready for more complex assignments.", color="green")
    else:
        typewriter("\nRecommend additional training before field work.", color="red")
    
    typewriter("\nCase details:", color="bold")
    for r in results:
        status = "SOLVED" if r['correct'] else "OPEN"
        color = "green" if r['correct'] else "red"
        typewriter(f"{r['case_id']}: {r['difficulty']} - {status} ({r['time']}s)", color=color)

if __name__ == "__main__":
    main()

