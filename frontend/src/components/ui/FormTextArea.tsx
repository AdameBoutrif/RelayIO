import React from "react";

interface FormTextAreaProps {
    label?: string;
    name?: string;
    value?: string;
    onChange: (e: React.ChangeEvent<HTMLTextAreaElement>) => void;
    placeholder?: string;
}

export function FormTextArea({ label, name, value, onChange, placeholder }: FormTextAreaProps) {
    return (
        <div className="flex flex-col gap-1">
            <label htmlFor={name} className="font-medium">
                {label}
            </label>
            <textarea
                id={name}
                name={name}
                value={value}
                onChange={onChange}
                placeholder={placeholder}
                className="border p-2 rounded"
            />
        </div>
    );
}