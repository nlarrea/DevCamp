import React, { Component } from 'react';

import JournalList from './journals/journal_list';

export default class App extends Component {
    render() {
        return (
            <div className='app'>
                <h1>React, Props & State - Deep Dive</h1>
                <JournalList heading='List 1' />
            </div>
        );
    }
}