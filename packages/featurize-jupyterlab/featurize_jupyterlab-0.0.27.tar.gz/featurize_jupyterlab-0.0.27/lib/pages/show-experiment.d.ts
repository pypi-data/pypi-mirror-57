import React from 'react';
import { match } from 'react-router-dom';
import ExperimentStore from '../store/experiment-store';
import { Experiment } from '../store/constant';
import { Subscribe } from '../utils';
interface ShowExperimentParams {
    id: string;
}
interface ShowExperimentProps {
    match?: match<ShowExperimentParams>;
}
interface ShowExperimentState {
    activeTab: string;
    experiment: Experiment;
    isDeleted: boolean;
    loading: boolean;
}
declare class ShowExperimentPage extends React.Component<ShowExperimentProps, ShowExperimentState> {
    id: string;
    experimentStore: ExperimentStore;
    subscription: Subscribe;
    constructor(props: ShowExperimentProps);
    refresh: () => Promise<void>;
    componentDidMount(): void;
    componentWillUnmount(): void;
    onRemark: () => void;
    onTabChanged: (activeKey: string) => void;
    onDelete: () => void;
    render(): JSX.Element;
}
export default ShowExperimentPage;
