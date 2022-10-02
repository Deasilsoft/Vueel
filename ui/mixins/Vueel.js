export default {
    data()
    {
        return {
            vueel: {
                Ts: {},
                Cs: {}
            }
        };
    },

    methods: {
        async T(key)
        {
            if (key in this.vueel.Ts)
            {
                return this.vueel.Ts[key];
            }

            const value        = await window.eel.T(key)();
            this.vueel.Ts[key] = value;

            return value;
        },

        async C(key)
        {
            if (key in this.vueel.Cs)
            {
                return this.vueel.Cs[key];
            }

            const value        = await window.eel.C(key)();
            this.vueel.Cs[key] = value;

            return value;
        },

        clear()
        {
            this.vueel.Ts = {};
            this.vueel.Cs = {};
        }
    }
};
