interface ReviewCardProps {
    name?: string;
    shot: string;
    task: string;
    awaitingDays: number;
}

export function ReviewCard({ name = "Review Card", shot = "SH000", task = "Department", awaitingDays = 0 }: ReviewCardProps) {
    return (
        <div className="rounded-xl flex flex-col w-48 h-48 items-center justify-between p-6 bg-slate-200 border border-slate-500 gap-2">
            <div>
                <div className="text-sm font-semibold uppercase tracking-wider text-gray-600">
                    {name}
                </div>
            </div>

            <div className="text-4xl font-extrabold text-slate-900 my-2">
                {shot}
            </div>

            <div>
                {task}
            </div>
            <div>
                Days Waiting: <span className="font-bold">{awaitingDays}</span>
            </div>
        </div>
    );
}