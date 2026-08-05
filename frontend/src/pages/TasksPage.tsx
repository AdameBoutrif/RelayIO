import { Navigation } from "../components/ui/Navigation"
import { TaskList } from "../components/tasks/TaskList"
import { TaskDetails } from "../components/tasks/TaskDetails"
import { useState } from "react"



export function TasksPage() {
    const [selectedTaskID, setSelectedTaskID] =
        useState<number | null>(null);

    return (
        <main className="p-6">
            <header>
                <Navigation />
            </header>

            <div className="flex gap-6 mt-6">
                <TaskList onSelectTask={setSelectedTaskID} clickedTaskID={selectedTaskID} />
                <TaskDetails taskId={selectedTaskID} />
            </div>
        </main>
    )
}
