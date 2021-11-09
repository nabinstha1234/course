import React from 'react';
import { useFormContext } from 'react-hook-form';
import ReactHookFormTextFieldMemo from './RHookFormTextFieldMemo';

interface ReactHookFormTextFieldContainerProps {
  name: string;
  label?: string;
}

const RHookFormTextFieldContainer = ({
  name,
  label,
}: ReactHookFormTextFieldContainerProps) => {
  const methods = useFormContext();
  return (
    <ReactHookFormTextFieldMemo
      methods={methods}
      label={label}
      name={name}
    />
  );
};

export default RHookFormTextFieldContainer;
