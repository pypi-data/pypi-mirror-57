import React from 'react';
import { getExperimentStore } from '../store';
import ExecutionStore from '../store/execution-store';
import { Popconfirm, Divider, Modal, Icon } from 'antd';
import { Link } from 'react-router-dom';
import { pendingStatus } from '../utils';
import RemarkModal from './remark-modal';
export default class Operations extends React.Component {
    constructor(props) {
        super(props);
        this.showBootModal = () => {
            return () => {
                const { experimentId } = this.props.execution;
                this.setState({
                    showBootModal: true,
                    devBootCommand: `featurize run --config /Users/louisshe/work/featurize-jupyterlab/.featurize_experiments/${experimentId}/runtime.config.json`,
                    bootCommand: `docker build http://demo.featurize.ai:8888/featurize/static/${this.props.execution.experimentId}/${this.props.execution.id}/docker.tar.gz`
                });
            };
        };
        this.stopExecution = () => {
            return () => {
                new ExecutionStore(this.props.execution.id).updateStatus('killing');
            };
        };
        this.onRemark = () => {
            this.setState({
                showRemarkModal: false
            });
            if (this.props.remarkCallback) {
                this.props.remarkCallback();
            }
        };
        this.experimentStore = getExperimentStore(this.props.execution.experimentId);
        this.experiment = this.experimentStore.getState();
        this.state = {
            showBootModal: false,
            showRemarkModal: false,
            bootCommand: '',
            devBootCommand: '',
        };
    }
    deleteExecution() {
        return async () => {
            await this.experimentStore.deleteExecution(this.props.execution.id);
            this.props.deleteCallback();
        };
    }
    render() {
        const { execution } = this.props;
        const { experimentId } = this.props.execution;
        const btnBoot = (React.createElement("a", { onClick: this.showBootModal() }, "boot"));
        const btnStop = (React.createElement(Popconfirm, { title: `Are you sure to stop execution ${execution.id}?`, onConfirm: this.stopExecution(), okText: "Yes", cancelText: "No" },
            React.createElement("a", null, "stop")));
        const btnDelete = (React.createElement(Popconfirm, { title: "Are you sure delete this Execution?", onConfirm: this.deleteExecution(), okText: "Yes", cancelText: "No" },
            React.createElement("a", null, "delete")));
        const btnEdit = (React.createElement(Link, { to: `/featurize/experiments/${experimentId}/edit/${execution.id}` }, "edit"));
        let btnGroups;
        switch (execution.status) {
            case 'not_running':
                btnGroups = (React.createElement(React.Fragment, null,
                    btnBoot,
                    React.createElement(Divider, { type: "vertical" }),
                    btnEdit,
                    React.createElement(Divider, { type: "vertical" }),
                    btnDelete));
                break;
            case 'running':
                btnGroups = (React.createElement(React.Fragment, null, btnStop));
                break;
            default:
                break;
        }
        return (React.createElement("div", { className: "operation-group" },
            pendingStatus(execution.status) ? React.createElement(Icon, { type: "loading" }) : btnGroups,
            React.createElement(Modal, { title: "Boot yourself", visible: this.state.showBootModal, footer: null, closable: true, onCancel: () => { this.setState({ showBootModal: false }); } },
                React.createElement("div", null,
                    React.createElement("p", null, "Run the following command on any machine which is with docker installed:"),
                    React.createElement("pre", { className: "featurize__command" }, this.state.bootCommand))),
            React.createElement(RemarkModal, { remarkable: "experiment", remarkableId: experimentId, afterSubmit: this.onRemark, visible: this.state.showRemarkModal, onCancel: () => { this.setState({ showRemarkModal: false }); } })));
    }
}
