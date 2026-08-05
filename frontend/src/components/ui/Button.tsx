interface ButtonProps {
    name: string;
    onClick?: () => void;

}

export function Button({ name = "Button", onClick }: ButtonProps) {
    return (
        <div onClick={onClick} className="w-48 h-12 flex rounded-3xl items-center justify-center bg-white/75 hover:bg-white cursor-pointer">
            {name}
        </div>
    );
}