import { memo } from 'react';
import { TextField } from '@material-ui/core';
import { UseFormReturn } from 'react-hook-form';

interface IReactHookFormTextFieldMemoProps {
  label: string | undefined;
  methods: UseFormReturn;
  name: string;
}

const ReactHookFormTextFieldMemo = memo(
  ({ label, methods, name }: IReactHookFormTextFieldMemoProps) => (
    <TextField
      label={label}
      variant="outlined"
      error={!!methods.formState.errors.message}
      helperText={methods.formState.errors.message?.message ?? ''}
      fullWidth
      margin="dense"
      {...methods.register(name)}
    />
  ),
  (prevProps, nextProps) => {
    return (
      prevProps.methods.formState.isDirty ===
        nextProps.methods.formState.isDirty &&
      prevProps.methods.formState.errors !==
        nextProps.methods.formState.errors
    );
  },
);

export default ReactHookFormTextFieldMemo;
