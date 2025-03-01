"""
Quest Status
Fantasy Quest needs a way to check the status of an individual character's quest status. The game stores each character's progress in a nested data structure, and your job is to fetch the status of a particular quest.

Here's the structure of a progress dictionary:

{
    "entity": {
        "character": {
            "name": "Kaladin",
            "quests": {
                "bridge_run": {
                    "status": "In Progress",
                },
                "talk_to_syl": {
                    "status": "Completed",
                },
            },
        }
    }
}

Assignment
Complete the get_quest_status function. It accepts a progress dictionary and returns the character's status in the "bridge_run" quest. Chain the keys to access the nested data.
"""

def get_quest_status(progress):
    return progress["entity"]["character"]["quests"]["bridge_run"]["status"]

