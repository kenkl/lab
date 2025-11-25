#!/usr/bin/env python3
"""This week's (2025-11-24) question:
Given an array of meal prep tasks for Thanksgiving, where each task is represented as [taskName, startTime, endTime], return the maximum number of non-overlapping tasks you can complete, along with the names of the chosen tasks in the order they were selected. Task times are inclusive of start but exclusive of end."""

tasks = [
  ["Make Gravy", 10, 11],
  ["Mash Potatoes", 11, 12],
  ["Bake Rolls", 11, 13],
  ["Prep Salad", 12, 13]
]

def maxMealPrepTasks(tasks):
    # Sort tasks by their end times
    tasks.sort(key=lambda x: x[2])
    
    selected_tasks = []
    last_end_time = -1
    
    for task in tasks:
        task_name, start_time, end_time = task
        if start_time >= last_end_time:
            selected_tasks.append(task_name)
            last_end_time = end_time
            
    return len(selected_tasks), selected_tasks

if __name__ == "__main__":
    max_count, chosen_tasks = maxMealPrepTasks(tasks)
    print("count:", max_count)
    print("chosen:", chosen_tasks)

