def appearance(intervals: dict[str, list[int]]) -> int:
    lesson_start, lesson_end = intervals['lesson']

    def process(intervals):
        its = sorted((intervals[i], intervals[i + 1]) for i in range(0, len(intervals), 2))
        merged = []
        for start, end in its:
            if not merged:
                merged.append([start, end])
            else:
                last_start, last_end = merged[-1]
                if start <= last_end:
                    merged[-1][1] = max(last_end, end)
                else:
                    merged.append([start, end])
        return merged

    pupil = process(intervals['pupil'])
    tutor = process(intervals['tutor'])

    total = 0
    i = j = 0
    while i < len(pupil) and j < len(tutor):
        p_start, p_end = pupil[i]
        t_start, t_end = tutor[j]

        # Находим пересечение с уроком
        start = max(lesson_start, p_start, t_start)
        end = min(lesson_end, p_end, t_end)

        if start < end:
            total += end - start

        # Переходим к следующему интервалу
        if p_end < t_end:
            i += 1
        else:
            j += 1

    return total
