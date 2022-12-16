import { FC } from 'react';
import Field from './Field';
import { Form } from '../types';

const Form: FC<Form> = ({ action, fields }) => {
    const onSubmit = (e) => {
        e.preventDefault();
        action();
    };

    return (
        <form onSubmit={(e) => onSubmit(e)} className="flex w-full">
            {fields.map(({ settings }: Field, idx) => (
                <Field
                    key={idx}
                    settings={{
                        type: settings.type,
                        placeholder: settings.placeholder,
                        className: settings.className,
                        state: settings.state,
                        setState: settings.setState,
                    }}
                />
            ))}
            <button type="submit" className="btn-blue ml-2">
                Send
            </button>
        </form>
    );
};

export default Form;
