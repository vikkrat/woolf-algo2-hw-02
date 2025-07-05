from typing import List, Dict
from dataclasses import dataclass

@dataclass
class PrintJob:
    id: str
    volume: float
    priority: int
    print_time: int

@dataclass
class PrinterConstraints:
    max_volume: float
    max_items: int

def optimize_printing(print_jobs: List[Dict], constraints: Dict) -> Dict:
    jobs = [PrintJob(**job) for job in print_jobs]
    jobs.sort(key=lambda x: x.priority)

    max_vol = constraints["max_volume"]
    max_items = constraints["max_items"]

    print_order = []
    total_time = 0
    used = [False] * len(jobs)

    for priority in sorted(set(job.priority for job in jobs)):
        while True:
            group = []
            volume_sum = 0
            count = 0
            for idx, job in enumerate(jobs):
                if not used[idx] and job.priority == priority:
                    if volume_sum + job.volume <= max_vol and count + 1 <= max_items:
                        group.append((idx, job))
                        volume_sum += job.volume
                        count += 1
            if not group:
                break
            time_group = max(job.print_time for _, job in group)
            total_time += time_group
            for idx, job in group:
                used[idx] = True
                print_order.append(job.id)

    return {
        "print_order": print_order,
        "total_time": total_time
    }
