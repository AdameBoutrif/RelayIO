import { Navigation } from '../components/generic/Navigation';
import { MetricCard } from '../components/MetricCard';
import { ReviewCard } from '../components/ReviewCard';
import { ActivityItem } from '../components/ActivityItem';

const metrics = [
    { name: "Outstanding Tasks", value: 24 },
    { name: "Tasks Awaiting Review", value: 12 },
    { name: "Overdue Tasks", value: 2 },
];

const reviews = [
    {
        shot: "SH010",
        task: "Hero Animation",
        waitingDays: 2,
    },
    {
        shot: "SH045",
        task: "Lighting",
        waitingDays: 1,
    }
];

const activities = [
    {
        name: "TSK001",
        artistName: "Ad Bou",
        activityName: "Rendered",
        shot: "SH030",
    },
    {
        name: "TSK002",
        artistName: "Frank Rey",
        activityName: "Published animation",
        shot: "SH060",
    },
    {
        name: "TSK003",
        artistName: "Bob Dyl",
        activityName: "Published environment",
        shot: "SH045",
    }
];

export function DashboardPage() {
    return (
        <main>
            <header>
                <h3>RelayIO</h3>
                <Navigation />
                <h2>Dashboard</h2>
            </header>

            <section>
                <h2 className="text-xl font-semibold">
                    Overview
                </h2>
                <div className="flex gap-4">
                    {metrics.map(metric => (
                        <MetricCard
                            key={metric.name}
                            name={metric.name}
                            quantity={metric.value}
                        />
                    ))}
                </div>
            </section>

            <section>
                <h2 className="mb-4 text-xl font-semibold">
                    Review Queue
                </h2>
                <div className="flex gap-4">
                    {reviews.map(review => (
                        <ReviewCard
                            key={review.shot}
                            shot={review.shot}
                            task={review.task}
                            awaitingDays={review.waitingDays}
                        />
                    ))}
                </div>
            </section>

            <section>
                <div>
                    <h2 className="mb-4 text-xl font-semibold">
                        Recent Activity
                    </h2>
                </div>
                <div className='flex flex-col gap-1'>
                    {activities.map(activity => (
                        <ActivityItem
                            key={activity.name}
                            name={activity.name}
                            artistName={activity.artistName}
                            activityName={activity.activityName}
                            shot={activity.shot}
                        />
                    ))}
                </div>
            </section>
        </main>
    );
}