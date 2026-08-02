interface NavigationProps {
    name?: string;
}

export function Navigation({ name = "Navigation" }: NavigationProps) {
    return (
        <div>{name}</div>
    );
}