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

export type Data = {
    label: string;
    value: number | string | null;
};

export type Dataset = Data[];

export type Panel = {
    settings: {
        name: string;
        data: Dataset | number | string | null;
    };
};

export type Box = {
    settings: {
        label: string;
        data: string | number | null;
    };
};
