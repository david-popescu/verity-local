import { FC } from 'react';
import Field from './Field';

const Form: FC<{ fields: Field[] }> = ({ fields }) => {
    return (
        <form action="" className="flex">
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
        </form>
    );
};

export default Form;
