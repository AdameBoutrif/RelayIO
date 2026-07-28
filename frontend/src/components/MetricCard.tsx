interface MetricCardProps {
    name: string;
    quantity: number;
}

export function MetricCard({ name = "Metric Card", quantity = 0 }: MetricCardProps) {
    return (
        <div className="rounded-xl flex items-center p-4 bg-slate-200 border border-slate-500">
            <div className="w-22 flex justify-center items-center shrink-0">
                <div className="text-4xl font-bold text-gray-1000 text-center">
                    {quantity}
                </div>
            </div>
            <div className="pl-2">
                <div className="text-xl font-medium text-gray-800">
                    {name}
                </div>
                <p className="text-sm text-gray-900">
                    Details
                </p>
            </div>
        </div>
    );
}