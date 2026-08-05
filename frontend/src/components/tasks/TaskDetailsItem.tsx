import { useState } from "react";

interface TaskDetailsItemProps {
    label: string;
    value: React.ReactNode;
}

export function TaskDetailsItem({ label, value }: TaskDetailsItemProps) {

    return (
        <div className="flex">
            <div className="flex h-12 w-64 items-center justify-center bg-white/25 font-bold">
                {label} :
            </div>
            <div className="flex h-12 w-64 items-center justify-center bg-white/50">
                {value}
            </div>
        </div>
    );
}