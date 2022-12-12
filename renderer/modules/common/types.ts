import { Dispatch, SetStateAction } from 'react';

export type Field = {
    settings: {
        type: string;
        state: string;
        setState: Dispatch<SetStateAction<string>>;
        placeholder?: string;
        className?: string;
    };
};

export type Form = {
    action: any;
    fields: Field[];
};
