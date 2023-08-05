import React from 'react';
import ExperimentStore from '../store/experiment-store';
import { Execution, Experiment } from '../store/constant';
interface OperationsProps {
    execution: Execution;
    statusCallback: (type: string) => any;
    deleteCallback: () => any;
    remarkCallback?: () => any;
}
interface OperationsState {
    showBootModal: boolean;
    showRemarkModal: boolean;
    bootCommand: string;
    devBootCommand: string;
}
export default class Operations extends React.Component<OperationsProps, OperationsState> {
    experimentStore: ExperimentStore;
    experiment: Experiment;
    constructor(props: OperationsProps);
    showBootModal: () => () => void;
    stopExecution: () => () => void;
    deleteExecution(): () => Promise<void>;
    onRemark: () => void;
    render(): JSX.Element;
}
export {};
