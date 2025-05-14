from pathlib import Path

# ML Model config
MODEL_DIR = Path(__file__).resolve().parent / 'weights'
DETECTION_MODEL = MODEL_DIR / 'best.pt'

# Disposal guidelines
DISPOSAL_GUIDELINES = {
    'cardboard_box': 'Flatten to save space and place in the recycling bin. Avoid if soiled with food or grease.',
    'can': 'Empty, rinse, and place in the recycling bin. Remove labels if possible.',
    'plastic_bottle': 'Rinse and remove the cap. Place both bottle and cap in the recycling bin unless otherwise stated.',
    'battery': 'Do NOT throw in regular trash. Take to a hazardous waste collection site or participating retailers.',
    'plastic_bag': 'Reuse if possible. Do not place in curbside recycling—drop off at designated store collection bins.',
    'light_bulb': 'Do not place in curbside bin. CFLs and LEDs should be taken to specific recycling centers or hardware stores.',
    'glass_bottle': 'Rinse and place in the recycling bin. Separate by color if required locally.',
    'electronics': 'Erase data and bring to an e-waste recycling facility. Many retailers also offer drop-off options.',
    'pizza_box': 'Recycle only the clean parts. If greasy or with leftover food, tear off and compost or dispose of soiled parts.',
    'styrofoam': 'Generally not recyclable curbside. Check for drop-off locations or reuse for insulation or packaging.',
    'paint_can': 'Let dry completely (if latex) and recycle the empty can. For oil-based paint, take to a hazardous waste facility.',
    'medication': 'Do not flush. Use drug take-back programs at pharmacies or police stations.',
    'clothing': 'Donate if wearable. Recycle at textile recycling centers or donation bins.',
    'printer_cartridge': 'Return to manufacturers or stores for recycling. Many offer mail-back programs.',
    'food_scraps': 'Compost at home or place in green bin if your city offers organics collection.',
    'paper_towel': 'Compost if unsoiled with chemicals. Do not recycle.',
    'tissue': 'Do not recycle. Compost if your municipality accepts it.',
    'aluminum_foil': 'Clean and ball it up. Recycle only if completely clean.',
    'plastic_utensils': 'Generally not recyclable. Reuse or place in trash if your local facility doesn’t accept them.',
    'diaper': 'Dispose of in regular trash. Do not attempt to recycle.',
    'ceramics': 'Not recyclable curbside. Donate if unbroken or dispose of in the trash.',
    'compact_disc': 'Take to e-waste recycling or reuse for crafts.',
    'bubble_wrap': 'Do not put in curbside recycling. Drop off at plastic film recycling locations.',
    'wine_cork': 'Compost natural corks or recycle through cork recycling programs.',
    'thermometer': 'Do not throw in trash if it contains mercury. Take to a hazardous waste facility.',

    # Guidelines for additional items from RECYCLABLE and NON_RECYCLABLE lists
    'plastic_bottle_cap': 'Remove and rinse. Check local guidelines, as some programs require recycling separately from the bottle.',
    'reuseable_paper': 'Use for notes or printing; if no longer needed, recycle as paper waste with minimal contamination.',
    'scrap_paper': 'Collect clean paper scraps for recycling. Avoid mixing with heavily soiled or contaminated paper.',
    'stick': 'If natural and untreated, compost if possible; otherwise, dispose of in regular trash.',
    'plastic_cup': 'Rinse and check the recycling symbol. If accepted by your local program, recycle; otherwise, dispose in trash.',
    'snack_bag': 'Often made from mixed materials. Dispose in regular trash due to contamination from food residues.',
    'plastic_box': 'Empty, rinse, and check for a recycling code. If accepted, recycle; if not, dispose in regular trash.',
    'straw': 'Typically not recyclable. Best disposed in regular trash; consider reusable alternatives.',
    'plastic_cup_lid': 'Rinse and check local guidelines. Often non-recyclable due to mixed plastics; dispose in trash if necessary.',
    'scrap_plastic': 'Small plastic fragments are often not accepted in curbside recycling. Dispose in regular trash or check for specialized programs.',
    'cardboard_bowl': 'If clean and free of food residue, recycle with paper products; if contaminated, compost or dispose in trash.',
    'plastic_cultery': 'Disposable plastic cutlery is generally not recyclable. Reuse if possible or dispose in regular trash.'
}

RECYCLABLE = ['cardboard_box', 'can', 'plastic_bottle_cap', 'plastic_bottle', 'reuseable_paper']
NON_RECYCLABLE = ['plastic_bag', 'scrap_paper', 'stick', 'plastic_cup', 'snack_bag', 'plastic_box', 'straw', 'plastic_cup_lid', 'scrap_plastic', 'cardboard_bowl', 'plastic_cultery']
