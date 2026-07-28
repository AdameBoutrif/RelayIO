interface ActivityItemProps {
    name: string;
    artistName: string;
    activityName: string;
    shot: string;
}

export function ActivityItem({ name = "TaskID", artistName = "Artist Name", activityName = "Activity item", shot = "SH000" }: ActivityItemProps) {
    return (
        <div className="rounded-md flex max-w-125 bg-slate-100/35 border border-slate-400">
            "{artistName}" {activityName} for {shot} - <div className="italic">{name}</div>
        </div>
    );
}