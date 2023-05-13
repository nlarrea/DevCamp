import React, { Component } from 'react';

export default class Discussion extends Component {
    constructor() {
        super();

        this.state = {
            pageTitle: 'Discussion',
            currentTime: String(new Date())
        };
    }
    
    /**
     * This function will update the time in the screen every
     * second.
     */
    componentDidMount() {
        this.liveTime = setInterval(() => {
            console.log('New chat message');
            this.setState({ currentTime: String(new Date( )) })
        }, 1000);
    }

    /**
     * This function stops the interval whenever we leave
     * the Discussion route.
     */
    componentWillUnmount() {
        clearInterval(this.liveTime);
    }
    
    render() {
        // object deconstruction
        const { pageTitle, currentTime } = this.state;

        return (
            <div>
                <h1>{pageTitle}</h1>
                <div>{currentTime}</div>
            </div>
        );
    }
}